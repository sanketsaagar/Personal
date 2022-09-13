#Rename a key of a Dictionary

student1 = {'Maths':34, 'Science':65, 'English':45, 'Hindi':76 }

print('The Original Dictionary is:- ', student1) #Printing the original Dictionary

student1['Social Science'] = student1['Science']

del student1['Science']

print('After Renaming the Dictionary :-', student1)
