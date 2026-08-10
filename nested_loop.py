#nested loop
#loop inside a loop
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)


# for i in range(1, 11):
#       for j in range(1,i+1):
#           print ("*",end="")
#       print()

# for i in range(5,0,-1):
#      for j in range(1,i+1):
#           print("*", end="")
#      print()


# for i in range(1,5):
#      for j in range(6-i):
#           print("_",end="")
#      for j in range(1,i+1):
#           print("* ",end=" ")
#      print()  


for i in range(1,8):
     for j in range(9-i):
          print(" ",end="")
     for k in range(1,i+1):
          print("* ",end=" ")
     print()       



#print chessboard pattern

for i in range(1,9):
     for j in range(1,9):
        if (i+j) %2==0:
            print("w",end=" ")
        else:
             print("b",end=" ")
     print()           
                   
# i      j
# 1 1 2 3 4 5 6 7 8     23456789
# 2 1 2 3 4 5 6 7 8     345678910
# 3 1 2 3 4 5 6 7 8     4567891011
# 4
# 5
# 6
# 7
# 8

#print H and I in *

