Dict = {'How are you?':'Fine thanks', ' What is your name?':'Buddy'}
s = input("Hello! Please ask a question:")
while(True):    
    if(s in Dict):
        print(Dict[s])
        s= input()

    elif(s=='Bye'):
        print("Nice talking to you visit again")
    break;

    else:
        print('Invalid Question')
    break;