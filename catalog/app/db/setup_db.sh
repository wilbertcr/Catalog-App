#!/bin/bash -x

# Lets make sure this script runs relative to this location
# regardless of where is called from.
cd $(dirname $0)

# Here we setup a password for vagrant and create our DB.
psql -f reset_database.sql
