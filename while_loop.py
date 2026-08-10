
#sum of digits in a number
#input=12345
#op=15
num=12345
sum=0
while num>0:
    b=num%10
    sum=sum+b
    #print(num)
    num=num//10
print(sum)


#reverse of a number 
#num=12345
#op=54321
num=12345
rev=0
while num>0:
    b=num%10
    rev=rev*10+b
    num=num//10
print(rev)    

#factorial of a number 
#num=4
#op=4*3*2*1

num=int(input("enter your number:-" ))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)    
