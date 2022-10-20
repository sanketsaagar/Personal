def listskills(val, list=[]):
    list.append(val)
    return list

list1 = listskills('nodejs')
list2 = listskills('java',[])
list3 = listskills('reactjs')
print("%s" %list1)
print("%s" %list2)
print("%s" %list3)

print ([i.lower() for i in "TURING"])

try:
    print("Hello")
except:
    print("An exception occur")
finally:
    print("world")

a = [1,2,3,4]
b= [sum(a[0:x+1]) for x in range(0, len(a))]
print(b)

x = "abcdef"
i = "a"
while i in x[:-1]:
    print(i, end= " ")
    