# #create a dictionary and print it
# dit={"name":"vaishnavi","age":20,"city":"satara"}
# print("dictionary:",dit)

# #Access a value using a key 
# student={"name":"vaishu","age":20}
# print("name:",student["name"])


# # Add new key pair
# student={"name":"vaishu","age":20}
# student["city"]="satara"
# print("updated student dictionary:",student)

# #updated an existing value
# student={"name":"vaishu","age":20}
# student["age"]=21
# print("updated student dictionary:",student)


# #remove a key-value pair
# student={"name":"vaishu","age":20,"city":"satara"}
# removed_value=student.pop("age")
# print(student)

# #loop through a dictionary
# student={"name":"vaishu","age":20,"city":"satara"}
# for key,value in student.items():
#     print(key,":",value)

#     #check if a key exits
#     student={"name":"vaishu","age":20,"city":"satara"}
#     if "age" in student:
#         print("key exists!")

#         #find dictionary length
#         student={"name":"vaishu","age":20,"city":"satara"}
#         print(len(student))


#         #get all keys or values
#         student={"name":"vaishu","age":20,"city":"satara"}
#         print(student.keys())
#         print(student.values())

#         #create a empty dictionary
#         student={}
#         print("empty dictionary:",student)

#         #count frequency of each integer in  a list
#         nums=[1,2,2,3,3,3]
#         freq={}
#         for num in nums:
#             freq[num]=freq.get(num,0)+1
#             print(freq)

            
# #combine two lists into a dictionary
# keys=["name","age","city"]
# values=["vaishu",20,"satara"]
# data=dict(zip(keys,values))

# #merge two dictionaries
# a={"x":1,"y":2}
# b={"y":3,"z":4}
# merged=a.copy()
# for key,value in b.items():
#     merged[key]=merged.get(key,0)+value
#     print(merged)

    
    #key with the highest value 

scores={'A':90,'B':80,'C':95,'D':85}
max_key=max(scores,key=scores.get)
print("hightest score:",max_key)

#two sum
nums=[2,7,11,15]
target=9
index_map={}
for i,num in enumerate (nums):
    diff=target-num
    if diff in index_map:
        print([index_map[diff],i])
        break 
    index_map[num]=i
        
        
