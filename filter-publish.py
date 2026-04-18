import os
import fnmatch

# --- CONFIG ---
ROOT_DIR = "./content"   # directory to scan
WHITELIST = [
    ".obsidian/snippets/*",
    "**/Animes.base",
    "**/Projects.base",
]
BLACKLIST = [
    "03 Bases/tn-*.base",
    "private/**",
    "*.bak",
    ".stversions/*"
]

DRY_RUN = False  # set to False to actually delete
VERBOSE = False

def matches_any(filepath, root, patterns):
    rel = os.path.relpath(filepath, root)
    return any(fnmatch.fnmatch(rel, pattern) for pattern in patterns)

def is_whitelisted(filepath):
    return matches_any(filepath, ROOT_DIR, WHITELIST)

def is_blacklisted(filepath):
    return matches_any(filepath, ROOT_DIR, BLACKLIST)


def has_publish_true(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return False

    if not lines or not lines[0].strip() == "---":
        return False

    # extract frontmatter
    frontmatter = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        frontmatter.append(line)

    # simple check (no YAML parser dependency)
    for line in frontmatter:
        if "publish:" in line:
            value = line.split("publish:", 1)[1].strip().lower()
            return value == "true"

    return False


def main():
    for root, _, files in os.walk(ROOT_DIR):
        for name in files:
            path = os.path.join(root, name)

            if is_whitelisted(path):
                if VERBOSE:
                    print(f"[KEEP: whitelist] {path}")
                continue

            if is_blacklisted(path):
                if VERBOSE:
                    print(f"[DELETE: blacklist] {path}")
                if not DRY_RUN:
                    os.remove(path)
                continue

            if has_publish_true(path):
                if VERBOSE:
                    print(f"[KEEP: publish] {path}")
                continue

            if VERBOSE:
                print(f"[DELETE] {path}")
            if not DRY_RUN:
                os.remove(path)


if __name__ == "__main__":
    main()
