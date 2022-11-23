# 5. ILLUSTRATION OF TEXT FILE PROGRAMMING-II
Develop a python program to do the following task:
- Create a text file with multiple lines of text in it and print the same,
  to the standard output device
- Copy all those lines that contain the word 'the' to a new file.

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
    data = f.readlines()
    print("-- lines.txt --")
    print("".join(data))
    print()

newlines=[]
for line in data:
    words = line.split()
    if "the" in words:
        newlines.append(line)

with open("new lines.txt", "w") as f:
    for line in newlines:
        f.write(line)

with open("new lines.txt") as f:
    data = f.read()
    print("-- new lines.txt --")
    print(data)
    print()
```

## OUTPUT
```
-- lines.txt --
Once upon a time
a man lived in the woods
He was a very old man
He was a 90 years old
He lived a happy life

-- new lines.txt --
a man lived in the woods


```
