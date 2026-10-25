# while True:
#     choice=int("1. Add a name\n 2.Display names\n 3.Edit a name\n4. Delete a name\n5. Exit\nEnter your choice: ")
#     match choice:
#         case 1:
#             print('Add')
#         case 2:
#             print("Read")
#         case 3:
#             print("Edit")
#         case 4:
#             print("Delete")
#         case 5:
#             break
#         case _:
#             print("Invalid entry")

# names=["Amal","Karthi"]
# while True:
#     choice=int(input("1. Add a name\n 2.Display names\n 3.Edit a name\n4. Delete a name\n5. Exit\nEnter your choice: "))
#     match choice:
#         case 1:
#             name=input("Enter a name: ")
#             names.append(name)
#         case 2:
#             print(format("sl.no.","<15"),format("Name"))
#             print('-'*25)
#             count=1
#             for name in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#         case 3:
#             print(format("Sl.No.","<10"),format("Name")) #print(f"{"Sl.No.":^10}{"Name":^10})
#             print('-'*25)
#             count=1
#             for x in names:
#                 print(format(count,"<10"),x) #(f"{count:<10}{name})
#                 count+=1
#             edit_index=int(input("Enter the sl.no. of the name that you want to edit: ")) - 1
#             new_name=input("Enter the new name:")
#             names[edit_index]=new_name
#         case 4:
#             print(format("Sl.No.","<10"),format("Name"))
#             print('-'*25)
#             count=1
#             for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#             delete_index=int(input("Enter the sl.no. of the name that you want to edit: ")) - 1
#             names.pop(delete_index)
#         case 5:
#             break
#         case _:
#             print("Invalid entry")


# #compact if statement
# number=8
# if number%2==0:
#     print("Even")
# else:
#     print("odd")

# is_even_or_odd = "Even" if number%2==0 else "odd"
# print(is_even_or_odd)



# n=int(input("Enter a multi digit number:"))
# # sum=0
# # while n>0:
# #     r=n%10
# #     sum+=r
# #     n//=10
# # else:
# #     print(f"sum is {sum}")

# rev=0
# while n>0:
#     r=n%10
#     rev=(rev*10)+r
#     n//=10
# else:
#     print("Reverse is",rev)

# # #iteration1
# # n=124
# # rev=0
# # r=124%10=4
# # rev=(0*10)+4=4
# # n=124//10=12

# #iteration1
# # n=12
# # rev=0
# # r=124%10=4
# # rev=(0*10)+4=4
# # n=124//10=12

# # #iteration1
# # n=124
# # rev=0
# # r=124%10=4
# # rev=(0*10)+4=4
# # n=124//10=12


# #list comprehension 
# # syntax [expression for item in iterable if condition]
# # below is the normal way we use to do
# l2=[45,86,97,41,37,54,20,36]
# even_numbers = []
# for x in l2:
#     if x%2==0:
#         even_numbers.append(x)
# print(even_numbers)

# l1=[45,86,97,41,37,54,20,36]
# new_list=[x for x in l1] #1st x to access we are creating a new list or copy of l1
# even_numbers=[x for x in l1 if x%2==0] # here after loop we write thecondition if its true then it can be accessed in 1st x otherwise if false will not be in x
# squared_numbers =[x*x for x in l1]
# print(new_list)
# print(squared_numbers)
# print(even_numbers)

# [45,86,97,41,37,54,20,36]
# ['odd','even','odd','odd','odd','even','even','even']

l1=[45,86,97,41,37,54,20,36]
# l2=[]
# for x in l1:
#     if x%2==0:
        
#         print("even")
#     else:
        
#         print("odd")
# print(l2)

even_or_add=['even' if x%2==0 else 'odd' for x in l1]
print(even_or_add)

