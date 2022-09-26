#Q3. Write a python Program to check if a subslist is present in a list or not

orgList = [2,4,5,8,7,1,6,9]
subList = [11,3,12]

print( "The Original list is:- " + str(orgList))
print("The Sublist is:- " +str(subList))


if(all(x in orgList for x in subList)):
        print("Yes SubList is part of OrgList")
else:
        print("No, SubList is not part of OrgList")



