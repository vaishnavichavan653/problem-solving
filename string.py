#write a program to take a number and print its data types
num=input("enter a number:")
print("type before conversion:",type(num))
num=int(num)
print("type after conversion:",type(num))


# #take input and print whether its integer or string
data=input("enter data:")
if data.isdigit():
    print("it is a integer")
else:
    print("it is a string")

    #create variable of different data  types
name="vaishnavi"
age=20
marks=85.96
it_passed=True
print(name,age,marks,it_passed)


#starting string
# given a string s return the reversed string
text=input("enter a string:")
rev=text[::-1]
print("reversr string:",rev)


# given a string determine if it reads the same forward and backward ignoring non-alphanumeric characters ansd case

text=input("enter a string:")
cleaned=''.join(ch.lower()for ch in text if ch.isalnum())
if cleaned==cleaned[::-1]:
    print("palindrome")
else:
    print("no palindrome")



#first unique character in a string
s=input("enter a string:")
for i in range(len(s)):
    if s.count(s[i])==1:
        print("first unique character:",s[i],"at index",i)
        break
    else:
        print("no unique character found")


        
    # take a strint input and print it
text=input("enter a string:")
print(text)
lenght=len(text)
print("length of string",lenght)


# count how many vowels and consonants the string has



#convert string to uppercase and lowercase and also reverse the string
text=input("enter a string:")
print("uppercase:",text.upper())
print("lowercase",text.lower())
rev=text[::-1]
print("reverse string:",rev)


# check if the string is palindrome or not
text=input("enter a string:")
rev=text[::-1]
if text==rev:
    print("palindrome")
else:
    print("not palindrome:")
    


# count how many times a particular character appears in string
s=input("enter a string:")
ch=input("enter a character to be counted:")
print(f"'{ch}'appears{s.count(ch)} times")

# replace all spaces in a string with hypens(_)
text=input("enter a sttring:")
rep=text.replace(" ","_")
print("new string:",rep)


# check if string starts or ends with a specific word
text=input("enter a string:")
start_word=input("enter starting word:")
end_word=input("enter ending word:")
print("start with",text.startswith(start_word))
print("end with",text.endswith(end_word))

#find the first non-repeating charater in a string
