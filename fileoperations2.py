# you can do 'from os import *' but sometimes this causes issues
import os

# Create a new directory and navigate into it
os.mkdir("newdirectory")
os.chdir("newdirectory")

# Create and write to a file in the new directory
with open('file.txt', 'w') as f:
    f.write("Hello World!")

os.rename("file.txt", "myfile.txt")
# os.remove("myfile.txt")
