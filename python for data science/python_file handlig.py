## Open a file and read its content:
s = open("demo.txt")
print(s.read())

s = open("/Users/jestin/Desktop/Python/python for data science/demo.txt")
print(s.read())

# using with statement to open a file
with open("demo.txt") as f:
    print(f.read())

    ## close files

# to read lines
f = open ('demo.txt')
print(f.readline())
f.close()

## read only parts of the file
with open("demo.txt") as f:
    print(f.read(10))

# read 2 or more lines at a time
with open("demo.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())


## By looping through the lines of the file, you can read the whole file, line by line:
with open('demo.txt') as f:
    for line in f:
        print(line)

 ## Write to an Existing File
 ## "a" - Append - will append to the end of the file
 ## "w" - Write - will overwrite any existing content

with open("demo.txt", "a") as f:
    f.write("this is a new line\n")


with open("demo.txt", "a") as f:
    print(f.read())
# Overwrite Existing Content
with open("demo.txt", "w") as f:
    f.write("this will overwrite the existing content\n")

## To create a new file in Python, use the open() method, with one of the following parameters:
## "x" - Create - will create a file, returns an error if the file exists
## "a" - Append - will create a file if the specified file does not exists
## "w" - Write - will create a file if the specified file does not exists

## creating new file with content
with open('newfile.txt', 'x') as f:
    f.write("this is a new file\n")

## creating new file called newfile2.txt
with open("newfile2.txt", "x") as f:
    f.write("this is another new file\n")

# Deleting a File. - must import os module to delete a file
import os
os.remove('newfile2.txt')

# Check if File exist:
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("file does not exist")


# Delete Folder

import os
os.rmdir("newfolder")

# create folder 
os.mkdir("newfolder")

os.mkdir("parent_folder/child_folder")
# This will not create an folder inside another folder. It will throw 
# an error if the parent folder does not exist.

# Create nested folders at once (e.g., folder1 containing folder2)
# -p is to create a new folder if it does not exist. If the folder already exists, it will not throw an error.
mkdir -p parent_folder/child_folder

# delete nested folders at once
rm -r parent_folder

# Option B: Recommended (Safe creation, won't crash if it already exists)
os.makedirs("parent_folder/child_folder", exist_ok=True)












