#!/usr/bin/env sh

rm -rf content
cp -al ~/Documents/notes content
python filter-publish.py
npx quartz sync
