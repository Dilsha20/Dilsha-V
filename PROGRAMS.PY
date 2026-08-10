
#1. #Find vowels and their position in a string
# # a=input("enter the string:")
# # count=(str(len))
# # for i in range(len(a)):
# #     if a[i] in "aeiou":
# #      print(f"'{a[i]}' at location {i}")

# # name=input("enter your name:")
# # for i in range(0,len(name)):
# #     if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
# #         print(i,name[i])


# # name=input("enter your name:")
# # for i in range(0,len(name)):
# #     if name[i]in "aeiou":
# #         print(i,name[i])

#2. #create a list of even numbers and odd numbers from first 100 numbers

# num=[]
# even=[]
# odd=[]
# for i in range(1,101):
#     num.append(i)
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)    

# 3.#c=[1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]  
# #remove duplicates from this list

# c=[1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# b=[]
# for i in c:
#     if i not in b:
#         b.append(i)
# print(b)

# input n words.make it into a sentence
# reverse of a string without using[::-1]



# 4. a=[11,13,14,15,16,17,18,19,20,12,15]
# mid=len(a)//2
# c=[]
# d=[]
# for i in range(len(a)):
#     if i<mid: 
#         c.append(a[i])
#     else:    
#         d.append(a[i])
# print(c) 
# print(d)

#5. a=[11,1,100,-900,10,15,16]
#print largestb and smallest int from this list
# largest=0
# smallest=0
# for i in a:
#     if i> largest:
#         largest=i
#     if i<smallest:
#         smallest=i    
    
# print(largest,smallest)

#sort a


#6.print I using *
# i=rows
# j=columns

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i== 5 or j == 3:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print() 

#7.
# *****
# *   *
# *   *
# *   *
# *****


# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()                          


#8.s using *
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==3 or i==5 or i==2 and j==1 or i==4 and j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()                          


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==3 or i==5 or i==2 and j==1 or i==4 and j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()