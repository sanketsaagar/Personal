def recursivefac(n):
    if (n==0):
        return 1

    else:
        return n*recursivefac(n-1)
    
n= int(input("Enter a number"))
recursionresult=recursivefac(n)
print("The factorial of the entered number is", recursionresult)
