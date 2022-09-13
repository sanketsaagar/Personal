#Delete a list of keys from a dictionary


student1 = {'Maths':34, 'Science':65, 'English':45, 'Hindi':76 }

print('The original List is :-', student1) #print the original list

Removing_list = ['Science', 'Hindi']

for key in Removing_list:
    del student1[key]

print('After deleting the key:- ', student1)

