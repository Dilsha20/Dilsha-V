#file handling
#read 
#write
#text based


#read
file1=open("data.txt","r")
print(file1.read())
file1.close()

#write
#overwrite
file2=open("myfile.txt","w")
file2.write("this month is july!!!!!!!!!")
file2.close()

file3=open("myfile.txt","a")
file3.write("\nhello ")

file4=open("myfile.txt","a")
for i in range(1,11):
    file4.write(f"\ndilsha{i}")
file4.close()    

