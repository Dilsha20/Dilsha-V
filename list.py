#list

#collection of data
#1.list can have any element of any size
#dsts=[1,1.2,"mohan",true,2,4,6,7,8]
#2.list are ordered
# a=[1,2,3,4]
# b=[5,6,7,8]
# print(a=b)
#3.list are indexed ,str, tuple
#  0,  1,2, 3,  4(index value)
#a=[11,12,13,14,15,16,17,18,19]
                 #   -4-3-2-1
# print(a)
# print(a[0]) #11
#index[start:stop:step]
# print(a[3:8])
# print(a[3:9:2])
# print(a[:3])
# print(a[5])
# print(a[::-1])#reverse
# b=[0,9,8,7,6,67,89,50,21,22,1,34]
# print(b[4])
# print(b[:7])
# print(b[::-2])
# print(b[2:8:2])

#4.list are mutable/changable
# a=[11,1,2,13,14,15]
# a[0]="mohan"
# print(a)
# #5.dynamic
# #the list change to small and large 
# #6.list are nested
# a=[11,12,[100,21,],14,15]
# print(a[2][0])
# #or
# b=a[2]
# print(b[0])

#inbuilt methods

#to add elements
 

 #append()
      # adds an elements to the end of the list
# a=[11,77,44,21,3,1]
# a.append(100)
# print(a)
# a.append(300)
# print(a)
  

 #extend()
        #adds an itreable to the list
# a=[11,12,13,14,15]
# a.extend([23])
# print(a)
# a.extend([50,"mohan",90])
# print(a)


  #insert(index,value)
# a=[11,12,3,14,15]
# a.insert(1,"mohan")
# print(a)
# a.insert(5,"abc")
# print(a)


#to remove elements

  #remove()
#to remove element
# a=[12,13,11,15,122,265,125]
# a.remove(13)
# print(a)
# a.remove(265)
# print(a)
  #pop()
 #pop(index)
 # the last element of the list remove
# a=[12,13,11,15,122,265,125] 
# a.pop()
# print(a)
# a.pop(4)
# print(a)


