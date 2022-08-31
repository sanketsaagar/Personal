#Q1 Get the nth element and nth from the last of tuple user input

s= ('Mango', 'Apple','watermelon','Banana')
n= int(input("Enter the n value"))

print(s)
print(*s)
print("Nth Element: ",s[n])
print("Nth last element: ",s[-1])
