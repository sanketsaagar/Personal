
str1 = "Parallelogram"
str_new= {}

for i in range(0,len(str1)-1):
    j= (str1[i]+str1[i+1])
    if j in str1:
        if j in str_new:
            str_new[j]+= 1
 #       print(i)
        else:
            str_new[j] = 1


print('The twp successive characters are :'+str(str_new))