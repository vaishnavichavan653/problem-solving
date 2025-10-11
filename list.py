#create a list and print all elements
# a=[10,20,30,40]
# print("list elements",a)

# find the length of the list
# a=[1,2,3,4,5]
# print("length of list:",len(a))


#access the first and last elementsof alist

# a=[1000,20,44,443,9]
# print("first element:",a[0])
# print("last element:",a[-1])

#add a new element to the list
# l=[10,20,30,40,]
# l.append(50)
# print("after adding element:",l)


#remove an element from the list
# l=[10,20,30,40,5,0]
# l.remove(30)
# print("after removing 30:",l)


#sort the list in ascending order
# l=[10,20,30,40,50,6,7,0,80,]
# l.sort()
# print("sorted list (asending):",l)

#sort the list in desending order
# a=[1,2,3,4,5,6,7,9]
# l.sort(reverse=True)
# print("sorted list(desending):",l)


#find the maximum and minimum number
# l=[20,30,405,5,67,0,23]
# print("maximum :",max(l))
# print("minimum:",min(l))


#calculate the sum and average of list elements
# list=[1,2,3,4,55,67,8,3,44]
# total=sum(list)
# average=total/len(list)
# print("sum:",total)
# print("average:",average)


#count how many times a particular elements appears
# list=[12,34,56,78,23,134,0,8,0]
# print("0 appears",list.count(0),"times")


#take 5 numbers form user input and store them in a list
# numbers=[]
# for i in range (5):
#     num=int(input("enter a number:"))
#     numbers.append(num)
#     print("numbers entered:",numbers)

    #find even and odd numbers in a list
# numbers=[12,13,14,15,16,27,28,19]
# even=[]
# odd=[]
# for i in numbers:
#         if i% 2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#             print("even numbers:",even)
#             print("odd numbers:",odd)


   #find positive and negative number in list
# numbers=[1,2,-3,-34,9,0,-8,-5]
# positive=[]
# negative=[]
# for i in numbers:
#     if i>=0:
#         positive.append(i)
#     elif i<0
#         negative.append(i)
#         print("positive numbers:",positive)

#         print("negative numbers:",negative)

        #removeduplicate from a list
# numbers=[1,2,3,44,21,2,2,3,4,5,2,]
# unique_number=list(set(numbers))
# print("list after removing duplicates:",unique_number)

#reverse a list without using reverse()function
# numbers=[1,2,3,45,6,5,34]
# reverse= numbers[::-1]
# print("reverse a list:",reverse)

#find the second largest and second smallest number
# numbers=[12,3,234,53,1,9,0]
# numbers.sort()
# print("second largest number:",numbers[-2])
# print("second smallest number:",numbers[1])

#merge two lists
# list1=[1,2,3]
# list2=[2,34,5]
# merged_list=list1+list2
# print("after merged list:",merged_list)


#find the common element between two lists
# list1=[1,2,3,4]
# list2=[7,6,5,4]
# common=list(set(list1)&set(list2))
# print("common elements",common)

#two list are equal or not
# list=[1,2,3,4,]
# list2=[1,2,3,4,5]
# if list==list2:
#     print("list are equal")
# else:
#     print("not equal")


#separate string and numbers from a mixed list
# mixed=[1,"vaishu",3,"sakshi",4]
# numbers=[]
# string=[]
# for item in mixed:
#     if isinstance(item,int):
#         numbers.append(item)
#     elif isinstance(item,str):
#         string.append(item)
#         print("numbers",numbers)
#         print("string:",string)


#find all pairs of numbers whose sum is equalto agiven value
# numbers=[2,4,3,5,7,8,9]
# target=10
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] + numbers[j]==target:
#             print(numbers[i],"+",numbers[j],"=",target)


        #rotate a listto the right by k positions
# numbers=[1,2,3,4,5,6,7]
# k=2
# k=k%len(numbers)
# rotated=numbers[-k:]+numbers[:-k]
# print("rotated list:",rotated)


#flatten a nested list
# nested=[1,[2,3],[4,5,[6,7]]]
# flat=[]
# def flatten(lst):
#     for item in lst:
#         if isinstance(item,list):
#          flatten(item)
#     else:
#         flat.append(item)
#         flatten(nested)
#         print("flated list:",flat)


#find the frequency of each element in a list
# numbers=[1,2,3,4,5,6,2,3,3]
# frequency={}
# for n in numbers:
#     frequency[n]=frequency.get(n,0)+1
#     print("frequency of each element:",frequency)




#find duplicate elements and print them only once
numbers=[1,2,3,2,4,5,6,7,6]
duplicates=[]
for n in numbers:
 if numbers.count(n)>1 and n not in duplicates:
     duplicates.append(n)
     print("duplicates element:",duplicates)