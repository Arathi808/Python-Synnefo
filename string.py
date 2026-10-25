name="Alan Mathew"
#     012345678910
course='Python Programming'
address="""
kochi
kerala
India
"""
#type casting
rno=str(8)

print(name,course,address)
print(type(name))
print(len(name))
print(len(course))
print(len(address)) 

print(name[0])
print(address[9])

#slicing start,end,step
print(name[0:5])
print(course[5:16])
print(course[5:16:2])
print(course[1:17:3])

print(name[-1]) 
print(name[-2]) 
# 'Python Programming'
print(course[-10:-1]) 
print(course[-10:-1:2])
print(course[:5])
print(course[5])
print(course[4:])
print(course[::2]) #slicing with step from start to end
print(course[::-1]) #reverse the string

name="AlaN matHew"
print(name.lower()) # converts the string to lowercase
print(name.upper()) # converts the string to uppercase
print(name.capitalize()) # converts the first character to uppercase and the rest to lowercase
print(name.title()) # converts the first character of each word to uppercase and the rest to lowercase
print(name.swapcase()) # swaps the case of each character
print(name.startswith('Ala')) # checks if the string starts with the specified substring
print(name.endswith('Hew')) # checks if the string ends with the specified substring
print(name.isalpha()) # checks if all characters in the string are alphabetic
print('654654'.isdigit()) # checks if all characters in the string are digits
print('hfs5444'.isalnum()) # checks if all characters in the string are alphanumeric
print(name.strip()+'dfdf') # removes whitespace from both ends of the string
print(name.lstrip()+'dfdf') # removes whitespace from the left end of the string
print(name.rstrip()+'dfdf') # removes whitespace from the right end of the string

print(name.split(' ')) # splits the string into a list of substrings using space as the delimiter
print(name.split('a')) # splits the string into a list of substrings using 'a' as the delimiter

words = ["Hello", "world"]#converts list to string
print(" ".join(words))

print("".join(name))
print('*'*8) # prints a string of 8 asterisks

print(str(9)+'hai') # converts the integer 9 to a string and concatenates it with 'hai'

print("A is",14,",which is greater than 100;",14>100) 
print(f"\n\nA is {14},\twhich is greater than 100:{14>100}") 