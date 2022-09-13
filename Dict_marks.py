#Create a dictionary with marks of a student in various subjects. Print the average marks of the student, Highest and lowest scoring
#subject,add scores of a new subject into the dictionary and copy the dictionary for another studenst.


from statistics import mean


student1 = {'Maths':34, 'Science':65, 'English':45, 'Hindi':76 }
student2=  {'Maths': 50, 'Science':74, 'English':36, 'Hindi':38}

print('The original Dictionary for Student 1 is ',student1) #Printing the entire Dictionary for Student 1
print('The original Dictionary for Student 1 is ',student2) #Printing the entire Dictionary for Student 2

res = 0
for val in student1.values():
    res += val

res = res/len(student1)

print('The Average of marks are :-' + str(res)) #Printing average of values

student1.update({'Physics': '68'}) #adding new subject marks in the Dictionary
print("The new String after adding key value is :-" ,student1)


#fin_mean = mean(student1, key= student1.get)
#print("Mean Scoring Subject :",fin_mean) 

print('Minimum scoring Subject is: ',min(student1.keys()))
print('Maximum scoring Subject is: ',max(student1.keys()))



