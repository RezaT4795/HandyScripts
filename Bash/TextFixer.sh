#!/bin/bash

# Create a temporary variable
newfile="test"
# Iterate through all files and directories inside the working directory. 
for file in $(find $(pwd)/* -name '*');
do
        FILE_NAME=$(echo $file) # Saving filename.
        if [[ ! $FILE_NAME == $(pwd)"/script.sh" ]]; then # Excluding the script itself.
                echo "Processing file:"
                echo $file
                sed -e "s/\r//g" $file > $newfile # Removes all occurances of the given string or statement (eg: CONTROL-M or ^M) and save it to a temporary file.
                rm $file # Removes the original file.
                mv $newfile $file # Renaming the new file to original name of the file.
        fi
done 