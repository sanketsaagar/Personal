Dict = {'Hey there, How are you?':'Fine thanks', 
        'What is your name?':'Sanket', 
        'Where are you from?':'Jharkhand',
        'How was your day?':'Awesome!'}

I = input("Hello! Please shoot question: ")
while(True):    
    if(I in Dict):
        print(Dict[I])
        I= input()
    elif(I=='See you'):
        print("Sure, See you later")
        break
    else:
        print('Please ask valid questions')