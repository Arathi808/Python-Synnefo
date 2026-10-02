#1.Arithmatic operators

#Addition +
a=10   #(a,b=10,3)
b=3
print(a+b)
#subtraction -
print(a-b)
#Multiplication *
print(a*b)
#Division /
print(a/b)
#Floor division //
print(a//b)
#Modulus %
print(a%b)
#Exponentiation **
print(a**b)

#take input from users and typecasting or type conversion
a=input("enter 1st no.")
b=int(input("enter 2nd no."))

print(2**3**4)
print(3+2**3-4)


# #2.Assignment operators

x=10
x+=5
x-=5
x*=2
x/=2
x%=2
x//=3
print(x)

#3 comparison operator
x=10
y=8

print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

#4. Logical operators

#logical not
x=10
y=5
print(not x>y)

#logical AND --> condition1 and condition2 and condition3
age=19
has_voter_id=True
print(age>=18 and has_voter_id==True)

#logical or-->condition1 or condition2
has_voter_id=True
has_pancard= False
print(has_voter_id or has_pancard)
print("hello \nworld\tpython")
print(age,has_pancard,has_voter_id,sep='\n')
#separate can be used to separate comma separated values-\n,-,

#5. Membership operators
#in
print("python" in "python programming")
print(4 in [4,8,56])
print(4 not in [4,8,56])
print("hello" not in "Hello world" )

#6. identity operators
p = 10
q = 10
r = [89,73,14]
s = [89,73,14]
print(p==q,end='-----')
print(p is q,end=' ')
print(r is s,end='///')
print(r == s)
print(id(r))
mark=45
grade=mark>40 and "A"
print(grade)
print("hai" and "hello")
print(1 and "hello")
print(0 and "hello")
#end is used to join the output of next print statement into the previous print statements output

print(bool(True))
print(bool(False))
print(bool("hello"))
print(bool(""))
print(bool(5456))
print(bool())
print(bool())
print(bool())
print(bool())

