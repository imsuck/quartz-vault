#!/usr/bin/env sh

rm -rf content
cp -al ~/Documents/notes content
python filter-publish.py
prettier content --write
npx quartz sync
