# #create a set and print all its element
# set={1,2,3,4,5}
# print("set elements:",set)


# #add an element to a set
# set={1,2,3}
# set.add(4)
# print("set after adding element:",set)

# #remove an element from a set
# set={1,2,3,4}
# set.remove(3)
# print("set after removing element:",set)

# #clear all elements from a set
# set={1,2,3,4,5}
# set.clear()
# print("set after clearing all elements:",set)

#check if element exists in a set
# set={1,2,3,4,5}
# element=3
# exists=element in set
# print("does element exist in set:",exists)

# #find the length of a set
# set={1,2,3,4}
# length=len(set)
# print("length of set:",length)

#convert a list to a set
# list=[1,2,2,3,4,4,5]
# set=set(list)
# print("set converted from list:",set)

# #create a set with mixed data types
# set={1,"hello",3.14,True}
# print("set with mixed data types:",set)


#use a loop to print all element in a set
# set={1,2,3,4,5}
# for element in set:
#     print("set element:",element)

    #check if a set is empty
# my_set=set()
# if not my_set:
#         print("set is empty")
# else:
#         print("set is not empty")

        #find the union of twop set
# set1={1,2,3,4}
# set2={3,4,5,6}
# union_set=set1.union(set2)
# print("union of set1 and set2:",union_set)

# # find the difference between two sets
# set1={1,2,3,4}
# set2={1,2,4,5,6}
# difference_set=set1.difference(set2)
# print("difference between set1 and set2:",difference_set)

# #find the symmetric difference between two sets
# set1={1,2,3,4}
# set2={3,4,5,6}
# symmetric_difference_set=set1.symmetric_difference(set2)
# print("symmetric difference between set1 and set2:",symmetric_difference_set)


# check if one set is a subset of another set
se1={1,2}
set2={1,2,3,4,5,6}
sub=set.issubset(set2)
print("is set 1 a is a subset of set 2:",sub)


# check if one set is a superset of another
set1={11,2,3,4,5}
set2={1,2,3,4}
print("is set1 ais a superset of set2:",set1.issuperset(set2))


# copy one set to another
set1={1,2,3,4}
set2=set1.copy()
print("set2 after copying set1:",set2)

#remove random element in a set
set1={1,2,3,4,5}
removed_element=set1.pop()
print("removed element:",removed_element)
print("remaning set element:",set1)

#update a set with multiple element
set1={1,2,3}
set1.update([4,5,6])
print("set after updating with multiple element:",set1)

#set comprehension
#create a square from 1to 10
square={x**2 for x in range(1,11)}
print("square set:",square)

#remove duplicate from a list using set
numbers=[1,2,3,3,4,6,7,6,9]
unique_numbers=list(set(numbers))
print("unique number:",unique_numbers)


#frozen set(immutable set)
fset=frozenset([1,2,3,4,])
print("frozen set:",fset)

#find common element in three set
a={1,2,3,4,5}
b={5,6,7,8,9}
c={5,2,6,7,1}
common=a & b & c
print("common element:",common)

#find element unique to each of two sets
a={1,2,3,45,2}
b={5,43,2,1,7}
unique=(a-b) | (b-a)
print("unique element:",unique)

#count unique word in sentence
sentence="python is easy and powerful language"
unique_words=set(sentence.split())
print("unique word:",unique_words)
print("count:",len(unique_words))

