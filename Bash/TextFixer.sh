#!/bin/bash

# Iterate through all files and directories inside the working directory. 
for file in $(find $(pwd)/* -name '*');
do
        FILE_NAME=$(echo $file) # Saving filename.
        if [[ ! $FILE_NAME == $(pwd)"/script.sh" ]]; then # Excluding the script itself.
                echo "Processing file:"
                sed -i -e 's/wrong//g' $file # Remove all occurances of the string (For example: "wrong" word).
                echo $file
        fi
done 
