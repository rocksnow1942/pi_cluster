#!/bin/bash

set -eEuo pipefail

# This script is used to upload the built artifacts to the Pi.

# then upload them to the Pi
# $1: pattern to match files
# $2: Pi's IP address

# first find file names that matches $1 regex pattern
find . -type f -name "$1" >/tmp/upload_files.txt

echo "Uploading files:"
cat /tmp/upload_files.txt

# confirm with user
read -p "Continue? (y/n) " -n 1 -r answer

if [[ ! $answer =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

rsync -avz --files-from=/tmp/upload_files.txt . $2:/home/hui/uploads/
# clean up
rm /tmp/upload_files.txt
