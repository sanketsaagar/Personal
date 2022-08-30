#Q4. Write a python program to perform cyclic rotation on a list of elements.


a=[]
size = int(input("Enter the size of List:- "))

for i in range(size):
    user= int(input("Enter the elements:- "))
    a.append(user)

print("Initial list")
for i in range(size):
    print(a[i], end=" ")

print("After rotation ")
x= a[size-1]

for i in range(size-1,0,-1):
    a[i]= a[i-1]
a[0]= x

for i in range(size):
    print(a[i], end=" ")
