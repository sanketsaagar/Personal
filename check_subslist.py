#Q3. Write a python Program to check if a subslist is present in a list or not

orgList = [2,4,5,8,7,1,6,9]

print( "The Original list is:- " + str(orgList))

subList = [5,8,6]

res = any(orgList[idx : idx + len(subList)] == subList
        for idx in range(len(orgList) - len(subList) + 1))
         
print("Is sublist present in list ? : " + str(res))



