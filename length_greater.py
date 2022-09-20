
str = " Hi, My name is sanket saagar karan"
n=3
print([word for word in str.split() if len(word)>n])
print([word for word in str.split() if len(word)<n])
