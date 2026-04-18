#!/usr/bin/env sh

rm -rf content
cp -al ~/Documents/notes content
rsync -avh --delete content/.obsidian/snippets/ quartz/styles/snippets/
python filter-publish.py
npx quartz sync
