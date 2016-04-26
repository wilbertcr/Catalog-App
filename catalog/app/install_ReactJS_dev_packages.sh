#!/usr/bin/env bash
# Install all app dependencies.
# --no-bin-links tells npm not to
# create any symbolic links, as npm
# breaks in vagrant when they're used.
npm install --save-dev --no-bin-links