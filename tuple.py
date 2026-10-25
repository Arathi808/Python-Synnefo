#tuple is a collection of heterogenous data. 
# ordered 
# indexed 
# allow duplicates 
# immutable
t1=(4,5,6,7,8,9,9,4,4,5,6,4)
print(t1)
print(len(t1))
print(type(t1))
print(t1[0])
print(t1[-1])
print(t1[0:3])#3 is excluded
print(t1[:5])#5 is excluded
print(t1[::-1])

# t1[2]=1  indexing not possible
# print(t1)

t2= 4,5,6,7,8 #packing
print(type(t2))
a,b=(4,5) #unpacking
print(a)
print(b)
name1,name2="Abin", "Alan"
print(t1.count(4))
print(t1.index(4))
print(t1.index(9))
print(len(t1))
for x in t1:
    print(x)

# l1=list('amal') #['a','m','a','l']
li=list(t1)   #to change a value in a index position we convert it to list then to tuple
# print(l1)
li[5]=19
# t1=tuple('amal')
t1=tuple(li)
print(t1)

names=['Aryan',"Arun","Anu","meenu","jethin"]
for index,name in enumerate(names):
    print(index,name)

#enumerate() adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object. 
# This is especially useful when you need both the index and the value of an item while looping through a collection.

names=['Aryan',"Arun","Anu","meenu","jethin"]
for name in enumerate(names): 
    print(name)

print(" ".join(names)) #list to string


for x in [[1,2,3],[4,5,6]]:
    for y in x:
        print(y)