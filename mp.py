#multiprocessing
# from multiprocessing import Process
# import os
# x=5
# def work():
#     global x #local to global
#     x=x*10
#     print("am working",x)
#     print(os.getpid())

# p1=Process(target=work)
# p2=Process(target=work)
# if __name__=="__main__":
#     print(x,"main process")
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()   



#list comprehension
#logic eyuthi create cheyyunnath
# a=[]
# for i in range(1,101):
#     a.append(i)
# print(a)  #normal list


# a=[i for i in range(1,101)]
# print(a) #list comprehension


# a=[i for i in range(1,101)if i % 2==0]
# print(a)

# # create a list with numbers that are multiples of 3 and 5
# a=[i for i in range(1,101) if i % 5 ==0 and i % 3==0]
# print(a)
# create a list of first 100 numbers that has digit 6 in them
# eg:-- [6,16,26,36...........996]
# a=[i for i in range(1,1000)if "6" in str(i)]
# print(a)

#regular expression

# import re
# pattern=r"\d{4}-\d{4}-\d{4}-\d{4}"
# #pattern=r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}"
# data="my adhaar number is 2435-3564-6789-9342"
# print(re.search(pattern,data))

# \d---oru decimal digit
# \w--alpha numeric
# \D-- no decimal digit
# \W -- no alpha numeric

# import re
# pattern=r"[a-z][A-Za-z0-9!#$%^&*()_+]+@[a-z]+.[a-z]+"  #[]+ --- for repeatation
# data=" my email is diSHa132567##$56&*^%$@gmail.com"
# print(re.search(pattern,data))



# import re
# pattern=r"([a-z][A-Za-z0-9!#$%^&*()_+]+)@([a-z]+).([a-z]+)"  #[]+ --- for repeatation
# data=" my email is diSHa132567##$56&*^%$@gmail.com, sJTMBGl34638$&*@gmail.com, dgjIKSGYD3258494#$^*@gmail.com"
# #z=re.findall(pattern,data)
# z=re.search(pattern,data)
# #1print(z)
# print(z.group(3))
# # for i in z:
# #     print(i)

#find website pattern eg-- https://www.google.com/

import re
pattern=r"([a-z]+://[a-zA-Z]+.[a-zA-Z0-9]+.[a-z]+/)"
data= "the website is https://www.google.com/"
print(re.search(pattern,data))
