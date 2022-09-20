
str1 = "Parallelogram"
str_new= {}

for i in str1:
    if i in str_new:
        str_new[i]+= 1
        print(str_new)
    else:
        str_new[i] = 1


print('The frequency of characters are :'+str(str_new))
#print("Maximum number of character is: ", max(str1.value()))