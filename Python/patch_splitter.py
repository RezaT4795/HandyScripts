from os import system

# Getting the content of the patch and splitting it.
diff_file = open('patch.diff', 'r')
diff_content = diff_file.read()
diff_splits = diff_content.split('diff --git')
diff_splits.remove(diff_splits[0]) # Removes the first element which is empty.
for i in range(len(diff_splits)):
    diff_splits[i] = "diff --git"+diff_splits[i] # Adds the missing "diff --git" at the beginning of all patch splits.

# Creating empty files and filling them with each patch split.
create_file = "touch "
for i in range(len(diff_splits)):
    # Changes file extentions to ".diff"
    # And name each file with a number, depending on the digits lenght of total patch splits.
    file_name = str(i+1).zfill(len(str(len(diff_splits))))+".diff" # Example: 01.diff, 02.diff,..., 99.diff 
    print("Splitting the patch [%s/%i]" % (file_name.removesuffix('.diff'), len(diff_splits))) # A simple progress indicator.
    empty_file = system(create_file+file_name)
    # Writing patch splits to each empty file after creation.
    result = open(file_name, 'w')
    result.write(diff_splits[i])
    result.close
