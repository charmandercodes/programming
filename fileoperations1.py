# WRITING 

with open('file.txt', 'w') as f:

    f.write("Hello my programmers!")

# APPENDING 

with open('file.txt', 'a') as f:

    f.write(" AppendeD")

# READING 
# The 'with' is used for automatic stream close

with open('file.txt', 'r') as f:

    content = f.read()

# You can the same without with
# but you have to make sure you close the stream

file = open("file.txt", 'r')
content = file.read()
file.close()

print(content)

# Notes 

# Why do we close?
# close calls flush that flushes from stream into file 
# calling flush itself does not close the stream, so you can still call from it 

# What if we append to a file that does not exist?
# it will create it 


# OTHER FILE OPERATIONS 

