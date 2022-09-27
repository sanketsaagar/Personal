#Python program to check if two strings become same after any number of cyclic rotation.

str1 = 'xyzk'
str2 = 'yzkx'

if len(str1)!= len(str2):
    print("The string is not same")

else:
     str1 = str1+str1
     if str1.index(str2):
         print("Yes, The string is same")
         
     else:
        print("No strings are not same")