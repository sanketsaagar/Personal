
#Q1. Remove even number from a list
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    if(i%2==0):
        a.remove(i)

print(a)
