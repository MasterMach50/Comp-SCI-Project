# 4. ILLUSTRATION OF TEXT FILE PROGRAMMING - I
Develop a python program to do the following tasks:
- Create a text file with multiple lines of text in it.
- Read the text File and display the number of vowels, consonants,
  lowercase, uppercase, spaces and digits in the file.

## Source Code
```py
# Create the file
with open("lines.txt", "w") as f:
    f.write("Once upon a time\n")
    f.write("a man lived in the woods\n")
    f.write("He was a very old man\n")
    f.write("He was a 90 years old\n")
    f.write("He lived a happy life")

with open("lines.txt") as f:
    data = f.read()
    print(data)
    print()

# variables for taking count
vowels = 0
consonants = 0
lcase = 0
ucase = 0
spaces = 0
digits = 0

for letter in data:
    if letter.isalpha():
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            vowels+=1
        else:
            consonants+=1
        
        if letter.isupper():
            ucase+=1
        if letter.islower():
            lcase+=1

    elif letter.isdigit():
        digits+=1

    elif letter.isspace():
        spaces+=1

print("There are", vowels, "vowels")
print("There are", consonants, "consonants")
print("There are", lcase, "lowercase letters")
print("There are", ucase, "uppercase letters")
print("There are", spaces, "spaces")
print("There are", digits, "digits")


```

## OUTPUT
```
Once upon a time        
a man lived in the woods
He was a very old man   
He was a 90 years old   
He lived a happy life   

There are 34 vowels
There are 45 consonants       
There are 75 lowercase letters
There are 4 uppercase letters 
There are 26 spaces
There are 2 digits
```
