# 12. ILLUSTRATION OF CSV FILE PROGRAMMING– II
# Develop a menu driven program implementing the user defined functions to perform
# different functions on a csv file named library.csv(bookid, bookname, noofcopies)
#     1. Append a record
#     2. Searching a record based on bookid
#     3. Display all
#     4. Exit

import csv

f = open("library.csv", "a") # Ensure that the file exists
f.close()

def appendBook():
    bID = input("Enter book ID: ")
    bName = input("Enter book Name: ")
    bCopy = input("Enter number of copies: ")

    with open("library.csv", "a", newline="") as f:
        wr = csv.writer(f)
        wr.writerow([bID, bName , bCopy])
    
    print("Record appended to file")

def searchBook():
    bID = input("Enter book ID: ")

    with open("library.csv", "r", newline="") as f:
        re = csv.reader(f)
        found = False # Using a loop to search for a values
        for row in re:
            if row[0] == bID:
                print("--------------------")
                print("bookID        :", row[0])
                print("Name          :", row[1])
                print("No of Copies  :", row[2])
                print("--------------------")
                found = True
                break
        if not found:
            print("Book with entered ID was not found")


def showBooks():
    with open("library.csv", "r", newline="") as f:
        re = csv.reader(f)
        for row in re:
            print("--------------------")
            print("bookID        :", row[0])
            print("Name          :", row[1])
            print("No of Copies  :", row[2])
            print("--------------------")

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Append a Book
    [2] Search for a Book
    [3] Show all Books
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        appendBook()
    
    elif ch == "2":
        searchBook()

    elif ch == "3":
        showBooks()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined


