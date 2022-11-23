# 6. ILLUSTRATION OF TEXT FILE PROGRAMING-III
Develop a program to create a text file to with a story in it and do the following tasks:
- To count the frequency of an inputted word in the file
- To read a random line and display it.

## Source Code
```py
import random

def create():
    with open("lines.txt", "w") as f:
        f.write("Once upon a time\n")
        f.write("a man lived in the woods\n")
        f.write("He was a very old man\n")
        f.write("He was a 90 years old\n")
        f.write("He lived a happy life")

def count():
    with open("lines.txt") as f:
        data = f.read()
        data = data.lower()
        words = data.split()
    
    chk_word = input("Enter word to count: ")
    count  = words.count(chk_word)

    print(chk_word, "appeared", count, "times")

def random_line():
    with open("lines.txt") as f:
        lines = f.readlines()
    
    num = random.randrange(0, len(lines))

    print("The random line is:")
    print("    ", lines[num])

create()

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Count the frequency of a word
    [2] Read a random line
    [3] Exit
    """)

    ch = input("Enter your choice[1/2/3]: ")

    if ch == "1":
        count()
    
    elif ch == "2":
        random_line()

    elif ch == "3":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined


```

## OUTPUT
```
=============================================
What would you like to do?

    [1] Count the frequency of a word
    [2] Read a random line
    [3] Exit
    
Enter your choice[1/2/3]: 1
Enter word to count: he
he appeared 3 times
=============================================
What would you like to do?

    [1] Count the frequency of a word        
    [2] Read a random line
    [3] Exit

Enter your choice[1/2/3]: 2
The random line is:
     Once upon a time

=============================================
What would you like to do?

    [1] Count the frequency of a word
    [2] Read a random line
    [3] Exit

Enter your choice[1/2/3]: 3
[ Exiting ]
```
