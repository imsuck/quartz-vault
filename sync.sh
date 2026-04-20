#!/usr/bin/env sh

rm -rf content
cp -al ~/Documents/notes content
prettier content --write
python filter-publish.py
npx quartz sync
