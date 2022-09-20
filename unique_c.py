
s1 = "Hello World!"

unique_characters = ""

for character in s1:
    if character not in unique_characters:
        unique_characters += character.lower()
print("Unique characters are : {} " .format(unique_characters))