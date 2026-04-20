#!/usr/bin/env sh

CACHE_DIR=node_modules/.cache/quartz

if [ -d ".quartz" ]; then
  rm -rf .quartz
fi

if [ -d "$CACHE_DIR" ]; then
  # [ -d .quartz ] && rm -rf .quartz
  # mv "$CACHE_DIR" .quartz
fi

if npx quartz plugin install && npx quartz build; then
  rm -rf "$CACHE_DIR"
  # [ -d .quartz ] && mv .quartz "$CACHE_DIR"
else
  echo "build failed, keeping old cache"
fi
