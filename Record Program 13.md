# 13. ILLUSTRATION OF CSV FILE PROGRAMMING– III
Develop a menu driven program implementing the user defined functions to perform different
functions on a csv file named contacts.csv(name, phone)
1. Append a contact
2. Count the number of contacts in the file
3. Display all contacts
3. Exit

## Source Code
```py
import csv

f = open("contacts.csv", "a") # Ensure that the file exists
f.close()

def appendContact():
    cName = input("Enter name: ")
    cNum = input("Enter number: ")

    with open("contacts.csv", "a", newline="") as f:
        wr = csv.writer(f)
        wr.writerow([cName, cNum])
    
    print("New Contact Added")

def countContacts():
    with open("contacts.csv", "r", newline="") as f:
        re = csv.reader(f)
        print("There are", len(list(re)), "contacts in the file.")


def showContacts():
    with open("contacts.csv", "r", newline="") as f:
        re = csv.reader(f)
        for row in re:
            print("--------------------")
            print("Name     :", row[0])
            print("Phone No :", row[1])
            print("--------------------")

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendContact()
    
    elif ch == "2":
        countContacts()

    elif ch == "3":
        showContacts()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined


```

## OUTPUT
```
=============================================
What would you like to do?

    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit
    
Enter your choice[1/2/3/4]: 1       
Enter name: Alice
Enter number: 1234567890
New Contact Added
=============================================
What would you like to do?

    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit

Enter your choice[1/2/3/4]: 1
Enter name: Bob
Enter number: 0987654321
New Contact Added
=============================================
What would you like to do?

    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit

Enter your choice[1/2/3/4]: 2
There are 2 contacts in the file.
=============================================
What would you like to do?

    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit

Enter your choice[1/2/3/4]: 3
--------------------
Name     : Alice
Phone No : 1234567890
--------------------
--------------------
Name     : Bob
Phone No : 0987654321
--------------------
=============================================
What would you like to do?

    [1] Append a Contact
    [2] Count the number of Contacts
    [3] Show all Contacts
    [4] Exit

Enter your choice[1/2/3/4]: 4
[ Exiting ]
```
