

#for loop
#for variable in iterable:
# body of loop

# for n in range(10):  #prints numbers from 0 to 9
#     print(n)

print('second loop')
for n in range(1,11):
    print(n)

print("Third loop")
for n in range(100,201):
    if n%2==0:
        print(n)

for n in range(1,6):
    print('*'*n)

for n in range(5, 0, -1):
    print('*'*n)

x=5
for n in range(5):
    print('*'*x)
    x-=1


for x in range(0,100,2):
    print(x)

#while
#while condition:
#   block if code
n=1
while n<=10:
    print(n)
    n+=1

n=1  
while n<=5:
    print('*'*n)
    n+=1

n=5 #pattern 5-1*
while n>=1: 
    print('*'*n)
    n-=1

#while condition
#   block of code

while 1<10:
    pass

n=1
while n<=10:
    if(n==4):
        break  #terminates a loop
    print(n)
    n+=1

n=1
while n<=10:
    if(n==4):
        continue  #skip an iteration
    print(n)
    n+=1

#trace
#iteration 1  
# n=1 
# 1<=10 -->true
#  1==4 -->false 
# n=2

#iteration 2
# n=2
# 2<=10 -->true
#  2==4 -->false 
# n=3

#iteration 3 
# n=3
# 3<=10 -->true
# 3==4 -->false 
# n=4

#iteration 4 
# n=4
# 4<=10 -->true
#  4==4 -->true
# n=4

#iteration 5           #the output:1 2 3
# n=4
# 4<=10 -->true
#  4==4 -->true
# n=4


#so the o/p will be 1 2 3 so t0 skip 4 and get reamining up to 10 below code
n=1
while n<=10:
    if(n==4):
        n+=1
        continue  #skip an iteration
    print(n)
    n+=1

#to get a sum of a number using loop
n=int(input("Enter a multi digit number: "))
sum=0
while n>0:
    r = n%10
    sum += r
    n//=10
    print(f"Sum is {sum}")

#iteration1 
# n=487
# sum=0 
# r=487%10 = 7 
# sum=0+7 
# n= 487//10 = 48

#iteration2
# n=48
# sum= 7
# r=48%10 = 8
# sum=8+7 = 15
# n= 48//10 = 4

#iteration3
# n=4
# sum=15
# r=4%10 = 4
# sum=15 +4 = 19
# n= 4//10 = 0

