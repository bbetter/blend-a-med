#!/bin/bash

# Get current date and time
now=$(date +"%Y-%m-%d_%H-%M-%S")

# Remove existing .zip files in the current directory
rm -f *.zip

# Create a directory with the current timestamp
mkdir blend-a-med

# Move all .py files to the newly created directory
cp -r *.py blend-a-med/

# Create a new zip archive with the current timestamp in its name
zip -r blend-a-med-${now}.zip blend-a-med/

# Count the number of .py files moved to the archive
num_files=$(find blend-a-med-${now}/ -type f -name '*.py' | wc -l)

# Print a message indicating the number of files that were added to the archive
echo "Added $num_files .py files to blend-a-med-${now}.zip"