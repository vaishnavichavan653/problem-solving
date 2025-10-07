# name=input("enter your name:")
# age=int(input("enter your age:"))
# marks=int(input("enter your marks:"))
# print("welcome",name)
# print("age=",age)
# print("marks=",marks)


# #take two number as input and print their sum
# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
# sum=num1+num2
# print("sum is:",sum)

#take two input number as  input and print the larger one
# a=int(input("entera number:"))
# b=int(input("enter a number:"))
# if a>b:
#     print("the larger number is a:",a)
# else:
#     print("the larger number is b:",b)

#     #take three subject marks as input and print the average
#     sub1=int(input("enter marks of sub1:"))
#     sub2=int(input("enter marks of sub2:"))
#     sub3=int(input("enter marks of sub3:"))
#     average=sub1+sub2+sub3/3
#     print("average of three subjects is:",average)

    #take a string and print how many charater it has
# text=input("enter a string:")
# length=len(text)
# print("enter number of charactres in string:",length)


#take a sentence and print how many words it contains

# sen=input("enter a sentences:")
# words=sen.split()
# print("how many words it contains:",words)


#take two number and print their diffrence,product ,quotient
# num1=int(input("enter a num1:"))
# num2=int(input("enter num2:"))
# difference=num1-num2
# product=num1*num2
# quotient=num1/num2
# print("diffrence is",difference)
# print("product is:",product)
# print("quotient is:",quotient)

#take a number and print whether it is positive,negative and zero
# x= float(input("enter a number:"))
# if x > 0:
#     print("number is positive:",x)
# elif x < 0:
#         print("number is negative:",x)
# else:
#         print("number is zero:",x)

        #take a number and print whether it is even or odd
# num=int(input("enter a number:"))
# if num%2==0:
#             print("number is even:",num)
# else:
#             print("number is odd:",num)

            #take a year and check ehether it is a leap year
# year=int(input("enter a year:"))
# if(year%4==0 and year%100!=0) or(year%400==0):
#                 print("leap year:",year)
# else:
#                 print("not leap year",year)



                #intermediate questions
                #take space-separated numbers and print their sum example:input=10 20 30 output=60
# number=list(map(int,input("enter number separatelyby space:").split()))
# total=sum(number)
# print("sum=",total)
#split() break input by space
#map(int,)converts each part into integer
#sum()adds all numbers


#take n numbers and print tne list
# n=int(input("enter a number of elements:"))
# nums=list(map(int,input("enter numbers:").split()))
# print("list=",nums)
#use first enters total count n
#then enters n space-separeted elements
#convrting to list using map()and list()


#take number as input and print only even numbers
# nums=list(map(int,input("enter a numbers:").split()))
# even_nums=[x for x in nums if x % 2==0]
# print("even numbers:",even_nums)


#take a sentence and count how many vowels are there
# text=input("enter a sentence:").lower()
# vowels="aeiou"
# count=0
# for ch in text:
#     if ch in vowels:
#         count+=1
#         print("number of vowels :",count)


#take a string and check whether its a palindrome
# s=input("enter a string:")
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


#take a list of names and print each name on a new line
# names=input("enter names seperately by space:").split()
# for name in names:
#     print(name)



    #take a matrix input (2Dlist)and print it 
    
    