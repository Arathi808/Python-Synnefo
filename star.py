# # for n in range(1,6):
# #     print('*'*n)

# # for n in range(5, 0, -1):
# #     print('*'*n)

# # x=5
# # for n in range(5):
# #     print('*'*x)
# #     x-=1

# n=1  
# while n<=5:
#     print('*'*n)
#     n+=1

# n=5 #pattern 5-1*
# while n>=1: 
#     print('*'*n)
#     n-=1

n = int(input("Enter n: "))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1