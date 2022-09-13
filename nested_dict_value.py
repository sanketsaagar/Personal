#Change value of a key in a nested dictionary

student1 = {'Ram':{'Height': '5','Colour':'White', 'Place':'Ranchi'},'Mohan':{'Height':'6','Colour':'Brown','Place':'Ramgarh'}}
print('Initial Dict is:-', student1)

student1['Mohan']['Colour'] = 'Dark'

print('The new Dic is :-', student1)