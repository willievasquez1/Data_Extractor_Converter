#!/bin/bash

# Navigate to the target directory
cd /Users/mdk/Documents/doc_data_extractor/output || { echo "Directory not found"; exit 1; }

# List the files in the directory
echo "Listing files in the directory:"
ls -al

# Display the contents of each file
echo "Displaying contents of each file:"
for file in *; do
  if [ -f "$file" ]; then
    echo "--------------------------------"
    echo "Contents of $file:"
    cat "$file"
    echo "--------------------------------"
  fi
done
