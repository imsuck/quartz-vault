#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
import yaml


CONFIG_FILE = "quartz.config.yaml"
LOCK_FILE = "quartz.lock.json"

LOCK_VERSION = "1.0.0"
MAX_WORKERS = 6

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


session = requests.Session()

session.headers.update({
    "Accept": "application/vnd.github+json",
    "User-Agent": "quartz-lock-generator",
})

if GITHUB_TOKEN:
    session.headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def load_yaml(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_lockfile(path: str) -> dict[str, Any]:
    if not Path(path).exists():
        return {
            "version": LOCK_VERSION,
            "plugins": {},
        }

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_lockfile(path: str, data: dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def parse_github_source(source: str) -> tuple[str, str]:
    """
    github:owner/repo
    -> (owner, repo)
    """

    if not source.startswith("github:"):
        raise ValueError(f"Unsupported source: {source}")

    repo_path = source.removeprefix("github:")

    parts = repo_path.split("/", 1)

    if len(parts) != 2:
        raise ValueError(f"Invalid GitHub source: {source}")

    return parts[0], parts[1]


def plugin_name_from_source(source: str) -> str:
    return source.rsplit("/", 1)[-1]


def get_latest_commit(owner: str, repo: str) -> str:
    url = f"{GITHUB_API}/repos/{owner}/{repo}/commits"

    response = session.get(
        url,
        params={"per_page": 1},
        timeout=15,
    )

    response.raise_for_status()

    commits = response.json()

    if not commits:
        raise RuntimeError(f"No commits found for {owner}/{repo}")

    return commits[0]["sha"]


def resolve_plugin(plugin: dict[str, Any]) -> tuple[str, dict[str, Any]] | None:
    source = plugin.get("source")

    if not source:
        return None

    owner, repo = parse_github_source(source)

    print(f"Resolving {owner}/{repo}...")

    commit = get_latest_commit(owner, repo)

    plugin_name = plugin_name_from_source(source)

    return (
        plugin_name,
        {
            "source": source,
            "resolved": f"https://github.com/{owner}/{repo}.git",
            "commit": commit,
            "installedAt": now_iso(),
        },
    )


def update_lockfile() -> None:
    config = load_yaml(CONFIG_FILE)
    lockfile = load_lockfile(LOCK_FILE)

    plugins = config.get("plugins", [])

    resolved_plugins: dict[str, Any] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(resolve_plugin, plugin)
            for plugin in plugins
        ]

        for future in as_completed(futures):
            try:
                result = future.result()

                if result is None:
                    continue

                plugin_name, plugin_data = result

                resolved_plugins[plugin_name] = plugin_data

            except requests.HTTPError as e:
                print(f"[error] GitHub API error: {e}")

            except Exception as e:
                print(f"[error] {e}")

    lockfile["version"] = LOCK_VERSION
    lockfile["plugins"] = resolved_plugins

    save_lockfile(LOCK_FILE, lockfile)

    print(f"Updated {LOCK_FILE}")

def pull_plugins():
    subprocess.run(
            "npx quartz plugin install --verbose",
            shell=True,
            check=True
        )

if __name__ == "__main__":
    update_lockfile()
    pull_plugins()

