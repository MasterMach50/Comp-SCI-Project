# 11. ILLUSTRATION OF CSV FILE PROGRAMMING– I
Develop a menu driven program implementing the user defined functions
to perform different functions on a csv file named mobile.csv(modelid, modelname, modelprice)
1. Append a record
2. Updating a record based on modelid
3. Display all
4. Exit

## Source Code
```py
import csv

f = open("mobile.csv", "a") # Ensure that the file exists
f.close()

def appendMobile():
    mID = input("Enter model ID: ")
    mName = input("Enter model Name: ")
    mPrice = input("Enter model Price: ")

    with open("mobile.csv", "a", newline="") as f:
        wr = csv.writer(f)
        wr.writerow([mID, mName , mPrice])
    
    print("Record appended to file")

def updateMobile():
    mID = input("Enter model ID: ")
    mName = input("Enter new model Name: ")
    mPrice = input("Enter new model Price: ")

    newrows = []
    with open("mobile.csv", "r", newline="") as f:
        re = csv.reader(f)
        for row in re:
            newrows.append(row)
    
    with open("mobile.csv", "w", newline="") as f:
        wr = csv.writer(f)
        for row in newrows:
            if row[0] == mID:
                wr.writerow([mID, mName , mPrice])
            else:
                wr.writerow(row)
    
    print("Updated record")
    print("--------------------")
    print("modelID:", mID)
    print("Name   :", mName)
    print("Price  :", mPrice)
    print("--------------------")

def showMobiles():
    rows = []
    with open("mobile.csv", "r", newline="") as f:
        re = csv.reader(f)
        for row in re:
            rows.append(row)
    
    for row in rows:
        print("--------------------")
        print("modelID:", row[0])
        print("Name   :", row[1])
        print("Price  :", row[2])
        print("--------------------")

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendMobile()
    
    elif ch == "2":
        updateMobile()

    elif ch == "3":
        showMobiles()

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

    [1] Append a Model      
    [2] Update a Model      
    [3] Show all Models     
    [4] Exit
    
Enter your choice[1/2/3/4]: 1
Enter model ID: 1
Enter model Name: Samsung S21
Enter model Price: 32000
Record appended to file
=============================================
What would you like to do?

    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit

Enter your choice[1/2/3/4]: 1
Enter model ID: 2
Enter model Name: IPhone 13
Enter model Price: 45000
Record appended to file
=============================================
What would you like to do?

    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit

Enter your choice[1/2/3/4]: 3
--------------------
modelID: 1
Name   : Samsung S21
Price  : 32000
--------------------
--------------------
modelID: 2
Name   : IPhone 13
Price  : 45000
--------------------
=============================================
What would you like to do?

    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit

Enter your choice[1/2/3/4]: 2
Enter model ID: 1
Enter new model Name: Samsung S21 Ultra
Enter new model Price: 44000
Updated record
--------------------
modelID: 1
Name   : Samsung S21 Ultra
Price  : 44000
--------------------
=============================================
What would you like to do?

    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit

Enter your choice[1/2/3/4]: 3
--------------------
modelID: 1
Name   : Samsung S21 Ultra
Price  : 44000
--------------------
--------------------
modelID: 2
Name   : IPhone 13
Price  : 45000
--------------------
=============================================
What would you like to do?

    [1] Append a Model
    [2] Update a Model
    [3] Show all Models
    [4] Exit

Enter your choice[1/2/3/4]: 4
[ Exiting ]
```
