#!/bin/bash

# Get current date and time
now=$(date +"%Y-%m-%d_%H-%M-%S")

rm -rf *.zip
# Create a list of all .py files in the current directory
py_files=$(ls *.py)

# Create a new zip archive called "python_files.zip" and add each .py file to it
zip blend-a-med-${now}.zip $py_files

# Print a message indicating the number of files that were added to the archive
num_files=$(echo $py_files | wc -w)
echo "Added $num_files .py files to blend-a-med.zip"