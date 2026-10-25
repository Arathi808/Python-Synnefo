# #collection
# #list-indexed, ordered, allow duplicates, can change value using index,mutable
# numbers = [45,870,110,134,1550,155]
# print(numbers)
# print(type(numbers))
# print(len(numbers))

# print(numbers[3])
# print(numbers[0:3])
# print(numbers[0:5:2])
# print(numbers[::-1])
# print(numbers[-1])

# numbers[2]=1
# print(numbers)

# for n in numbers:
#     print(n)

# print('Even numbers')
# for n in numbers:
#     if n%2==0:
#         print(n)

#methods
#append (x)= add one iem at the end
# list=[1,2,35,12]
# list.append(30)
# print(list)

# #extend(iterable) = add multiple items 
# list=[1,2,35,12]
# list.extend([8,9])
# list.extend("arathi")
# list.extend(["aru","anu"])
# print(list)

# #insert(i,x) = insert at index i, other elements shift right and dont replace 
# list=[1,2,35,12]  #(1,10)=[1,10,2,35,12]
# list.insert(1,10)
# print(list)

# #remove(x)= removes first matching value, raises valueError if absent
# list=[1,2,35,2,12]
# list.remove(2)
# print(list)

# #pop(i)= remove item at that index
# list=[1,2,35,12]
# list.pop(3)  #pop()=defaults to last item
# print(list)

# #clear()=remove all items
# # list=[1,2,35,12]
# # list.clear()
# # print(list)

# #index(x)=find first matching index
# list=[1,2,35,12]
# print(list.index(35))
# print(list)

# #count(x)=count matching values and returns an integer
# list=[1,2,35,12,44,44]
# print(list.count(44))
# print(list)

# #sort()=sorts list in place
# list=[1,2,35,12]
# list.sort() #ascending
# list.reverse() #descending
# list.sort(reverse=True) #descending
# print(list)

# # #reverse()= reverses the list
# # list=[1,2,35,12]
# # list.reverse()
# # print(list)

# #copy()=shallow copy
# list=[1,2,35,12]
# list2=list.copy()
# print(list)

# names=["Aryan","Arun","Anu","Meenu","Riya","Yamal"]
# names.append("Riya")
# names.append("Amal")
# names.insert(3,"Athul")
# names.extend(["surya","vijay","Ajith","ali","Athul"])
# names.remove("ali")
# names.pop(2)
# # names.pop()
# # del names[8]
# #del names
# #names.clear()
# print(names.index("surya"))
# print(names.count("Athul"))
# #names.sort()
# #names.reverse()
# names.append([1,2,3])
# copy_names=names.copy()
# copy_names[5]="Yadhu"
# names[-1][2]=86
# print(names[-1])    
# print(copy_names)

#to print names starting with letter A
names=["Aryan","Arun","Anu","Meenu","Riya","Yamal"]
for name in names:
    if name[0]=="A":
        print(name)

            #or

for name in names:
    if name.startswith('A'):
        print(name)
