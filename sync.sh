#!/usr/bin/env sh

rm -rf content
cp -al ~/Documents/notes content
npx quartz sync
