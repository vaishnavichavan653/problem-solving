    #create a tuple and print all elements
# a=(12,34,0,9,8,4)
# print("all elements in tuple:",a)

  #find the lenght of tuple
# b=(1,2,3,44,55,21)
# length=len(b)
# print("length of tuple:",length)

#acess first and last element in the tuple
# tul=(98,66,44,355,2,24,233)
# print("first element :",tul[0])
# print("last element:",tul[-1])

#convert a tuple into list vice versa
# num=(12,3,4,121,44,22,55)
# lis=list(num)
# new=tuple(lis)
# print("list:",lis)
# print("tuple:",new)

# #check if an element exists in a tuple
# tuple=(10,20,23,4,2,0,1,20)
# if 20 in tuple:
#  print("element present")
# else:
#  print("element not present")


 #cout how many times an element appears
#  x=(23,4,5,51,4,4,23,44,90,43)
#  print("4 appears",x.count(4),"times")

 #find index of particular element
# tul=(12,32,43,11,30)
# print("the index of 30 is:",tul.index(30))

# #join two tuples
# tuple1=(12,32,45,13,25,121)
# tuple2=(10,20,30,40,50,60,70)
# join=tuple1+tuple2
# print("join two tuple:",join)

# #repeate a tuple multiple times
# tup1=(12,32,45,13,25,121)
# repeated=tup1*3
# print("repeated tuple is:",repeated)


#slice tuple
# a=(12,32,45,13,25,121)
# print("sliced tuple:",a[1:3])


#take 5 number in user and store them in a tuple
# numbers=tuple(int(input("enter a numbers:"))for _ in range(5))
# print(" tuple:",numbers)

#find maximum and minimum element in a tuple
# number=(12,32,45,43,14,62,143)
# print("maximum element:",max(number))
# print("minimum element:",min(number))

#sort element of a tuple (by converting to list)

# number=(12,32,45,43,14,62,143)
# sorted_list=sorted(number)
# sorted_tuple= tuple (sorted_list)
# print("sorted tuple:",sorted_tuple)

# #find the sum and average of elements
# numbers=(12,23,45,12,31,22,2)
# total=sum(numbers)
# average=total/len(numbers)
# print("sum:",total)
# print("average",average)

# #create a nested tuple and access inner elements
# nested=(1,2,(3,4,5),6)
# print("inner tuple:",nested[2])
# print("access inner element 4:",nested[2][1])


# #remove an element from a tuple(by converting to list)
# my_tuple=(10,20,30,40)
# my_list=list(my_tuple)
# my_list.remove(30)
# new_tuple=tuple(my_list)
# print("Tuple after removal:",new_tuple)

#unpack a tuple into variable
# person=("Amar",20,"engineer")
# name,age,profession=person
# print("name:",name)
# print("age:",age)
# print("profession:",profession)


# #find the common elements between two tuple
# tuple1=(1,2,3,4,5)
# tuple2=(3,4,5,6)
# common=tuple(set(tuple1)&set(tuple2))
# print("common elements:",common)

# #check if all elements in a tuple arethe same
# my_tuple=(5,5,5,5)
# if all(x==my_tuple[0] for x in my_tuple):
#   print("all element are the same")
# else:
#   print("element are different")

#   #reverse tuple
# tuple=(12,21,32,1,2,9,80,43)
# reversed=tuple[::-1]
# print("reversed tuple:",reversed)


# #find element frequency in a tuple using dictionary
# tup=(1,2,2,2,2,3,3,3,3)
# freq={}
# for item in tup:
  # freq[item]=freq.get(item,0)+1
  # print("frequency of element:",freq)


  # #swap two tuples without usinga third variable
  # a=(1,2,3)
  # b=(4,5,6)
  # a,b=b,a 
  # print("a:",a)
  # print("b:",b)

  
  # # convert a listof tuples into a dictionary
# pair=[("a",1),("b",2),("c",3)]
# result=dict(pair)


?