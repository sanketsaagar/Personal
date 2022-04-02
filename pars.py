spam = "A B C D"
eggs = "E-F-G-H"

# the split() function will return a list
spam_list = spam.split()
# if you give no arguments, it will separate by whitespaces by default
# ["A", "B", "C", "D"]

eggs_list = eggs.split("-", 3)
# you can specify the maximum amount of elements the split() function will output
# ["E", "F", "G"]