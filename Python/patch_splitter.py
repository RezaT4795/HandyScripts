from os import system

# Getting the content of the patch and splitting it
diff_file = open('patch.diff', 'r')
diff_content = diff_file.read()
diff_splits = diff_content.split('diff --git')
diff_splits.remove(diff_splits[0])
for i in range(len(diff_splits)):
    diff_splits[i] = "diff --git"+diff_splits[i]

# Creating empty files and filling them with each split
create_file = "touch "

for i in range(len(diff_splits)):
    file_name = str(i+1).zfill(len(str(len(diff_splits))))+".diff"
    print("Splitting the patch [%s/%i]" % (file_name.removesuffix('.diff'), len(diff_splits)))
    empty_file = system(create_file+file_name)
    # Writing content to each empty file after creation
    result = open(file_name, 'w')
    result.write(diff_splits[i])
    result.close
