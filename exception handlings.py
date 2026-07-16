   #exception handling
#events that affect the execution of our program
#errors
#syntsx error
#type error
#intentation error

try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print("you have an error",e)
print("mohan")        


try:
    a=5
    b=1
    print(a/b)
except Exception as e:
    print("you have an error",e)
print("mohan")     

#multiple exceptions
#1.
try:
    a=int(input("enter :---"))
    b=5
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide a number with zero")
except ValueError:
    print("check values")
except TypeError:
    print("check types")
finally:
    print("this will always execute")     
      
#2.
try:
    a=int(input("enter :---"))
    b=5
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide a number with zero")
except ValueError:
    print("check values")
except TypeError:
    print("check types")
finally:
    print("this will always execute")    
                 
#3.
try:
    a=int(input("enter :---"))
    b="ambi"
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide a number with zero")
except ValueError:
    print("check values")
except TypeError:
    print("check types")
finally:
    print("this will always execute")  

#4.
try:
    a=int(input("enter :---"))
    b=0
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide a number with zero")
except ValueError:
    print("check values")
except TypeError:
    print("check types")
finally:
    print("this will always execute")

#raise keyword
class myerror(Exception):
    pass 
name="das"
if name=="das":
    raise myerror("name should not be das")