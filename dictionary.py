#key value pairs

student={
    "name":"Amal",
    "age":18,
    "rno":2,
    "course":"BCA",
    "course":"Bcom"
}

items=student.items()
# print(student)
# print(type(student))
# print(student["age"]) #gives key's value

student["name"]="AMal siby" #to change the name
# print(student["name"])

student["email"]="amal@gmail.com" #to add a ney key value
# print(student)

# print("BCA" in student) #false
# for x in student: #prints all the value only
#     print(student[x])

print(student['age'])
print(student.get('age'))
print(student.get('agee')) #gives none if key is not in dict
print(student.get('agee',20))#given a default value 20 if key value not in dict

student.update({"hobbies":("Reading","writing")})
student.update({'rno':4}) #updates key:value

student.setdefault("course","BBA") #checks if key course is there if not then only add bba
# print(student)
student.pop('rno')#removes the key we chose
print(student)

student.popitem() #removes the last key value pair
print(student)

print(student.values()) #print only values in list
print(student.keys()) #print only keys in list
print()

for key,value in items:
    print(f"{key}:{value}") #dict_items([(key,value),()]
