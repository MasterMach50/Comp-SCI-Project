# 2.ILLUSTRATION OF FUNCTION PROGRAMMING (USING LIST)
Develop a Python Program whicondition includes two user defined functions namely,
- create()- to create a list of roll numbers(integers)
- findroll()- to searcondition for a particular roll in a list

## Source Code
```py
rolls = []

def create():
    while True:
        num = int(input("Enter roll number: "))
        rolls.append(num)
        ch = input("Would you like to add another number: ")
        if ch.lower() != "y":
            break

def findroll():
    num = int(input("Enter roll number to search for: "))
    if num in rolls:
        print("Entered roll number was found at index", rolls.index(num))
    else:
        print("Entered roll number was not found in list")

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Create roll number list
    [2] Find roll number
    [3] Exit
    """)

    ch = input("Enter your choice[1/2/3]: ")

    if ch == "1":
        create()
    
    elif ch == "2":
        findroll()

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

    [1] Create roll number list
    [2] Find roll number       
    [3] Exit
    
Enter your choice[1/2/3]: 1    
Enter roll number: 1
Would you like to add another number: y
Enter roll number: 2
Would you like to add another number: y
Enter roll number: 3
Would you like to add another number: y
Enter roll number: 4
Would you like to add another number: n
=============================================
What would you like to do?

    [1] Create roll number list
    [2] Find roll number
    [3] Exit

Enter your choice[1/2/3]: 2
Enter roll number to search for: 3
Entered roll number was found at index 2
=============================================
What would you like to do?

    [1] Create roll number list
    [2] Find roll number
    [3] Exit

Enter your choice[1/2/3]: 2
Enter roll number to search for: 7
Entered roll number was not found in list
=============================================
What would you like to do?

    [1] Create roll number list
    [2] Find roll number
    [3] Exit

Enter your choice[1/2/3]: 3
[ Exiting ]
```
