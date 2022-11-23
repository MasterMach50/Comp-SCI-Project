# 10. SEARCH OPERATION USING DICTIONARY OBJECT
# A binary file named "emp.dat" contain certain records of employees (empid, empname and salary).Write a menu driven python program to do the following tasks:
#     1. Append a record
#     2. Search a record
#     3. Read and display all

import pickle

f = open("emp.dat", "a") # Ensure that the file exists
f.close()

def appendEmp():
    empID = int(input("Enter employee ID: "))
    empName = input("Enter emp name: ")
    salary = int(input("Enter emp salary: "))


    with open("emp.dat", "ab") as f:
        pickle.dump({"empID":empID, "empName":empName, "salary":salary}, f)

def searchEmp():
    emps = []
    with open("emp.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                emp = pickle.load(f)
                emps.append(emp)
            except:
                break
    
    empID = int(input("Enter employee ID: "))

    found = False # Using a loop to search for a values
    for item in emps:
        if item["empID"] == empID:
            print("--------------------")
            print("ID    :", item["empID"])
            print("Name  :", item["empName"])
            print("Salary:", item["salary"])
            print("--------------------")
            found = True
            break

    if not found:
        print("Employee not found")

def showEmps():
    emps = []
    with open("emp.dat", "rb") as f:
        while True:
            try: # Using a try block to catch errors
                emp = pickle.load(f)
                emps.append(emp)
            except EOFError:
                break
    for item in emps:
        print("--------------------")
        print("ID    :", item["empID"])
        print("Name  :", item["empName"])
        print("Salary:", item["salary"])
        print("--------------------")



while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append an employee
    [2] Search for an employee
    [3] Show all employees
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendEmp()
    
    elif ch == "2":
        searchEmp()

    elif ch == "3":
        showEmps()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined
