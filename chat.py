Dict = {'How are you?':'Fine thanks', 
        'What is your name?':'Sanket', 
        'Where are you from?':'Jharkhand',
        'How was your day?':'Awesome!',
        'What is 5+4?':9}

I = input("Hello! Please shoot questions : ")

while(True):    
    if(I in Dict):
        print(Dict[I])
        I= input("Next Question please : ")
    elif(I=='See you'):
        print("Sure, See you later")
        break
    else:
        print('Please ask valid questions from next time!')
        break