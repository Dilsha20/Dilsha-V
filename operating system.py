#os
import os

# os.mkdir("images")#make a directory(new file)
# os.remove("data.txt")#remove file
# os.rename("myfile.txt","demo.txt")#rename the existing file 
pat="C:\\Users\\hp ss\\OneDrive\\Desktop\\Python"
if os.path.exists(pat):
    if os.path.isfile(pat):
        print("file exists")
    elif os.path.isdir(pat):
        print("folder exists")    
