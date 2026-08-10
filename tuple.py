#tuple

#collection of data
# a=(2,3,1,"mohan")
# #ordered
# #indexed
# #immutable

# a=(1,2,3,4)
# #a[0]=10 this not possible in tuple
# print(a) 


#2 boxes

#elastic box- list
#metal box - tuple


#itration

# a=[11,12,15,17,18,165,16]
# b=["mohan das"]
# c=[100,200,300,400,500,600]
# # for i in a:
# #     print(i)

# for i in c:
#     print(i)    

# a="mohan"
# print(a[0])
# print(len(a)) 
# for i in range(0,len(a)):
#     print(i,a[i])

# fruits=["apple","orange","banana","pineapple","mango"]
# for i in range(0,len(fruits)):
#     print(i,fruits[i])


# num=15345
# count=0
# while a>0:
#     count=count+1
#     num=num//10
#     print(count)
    #amstrong number
# a=[1222]
# count=0
# for i in range(0,a):
#     count=count+1
#     a=a//10
#     print("i")

# b=153
# temp=b
# sum=0
# for i in range(temp):
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if (b==sum):
#     print("armstrong")
# else:
#      print("not armstrong")
  
  
  
# prime number   

# num=int(input('enter your number:--'))
# prime=True
# if num==1:
#     prime=False
# else:
#     for i in range(2,num):
#         if num%i==0:
#             prime=False 
#             break
# if prime==True:
#     print("prime number") 
# else:
#     print("not a prime") 



#or

num=int(input('enter your number:--'))
if num ==1:
   print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")    