# 2.ILLUSTRATION OF FUNCTION PROGRAMMING (USING LIST)
# Develop a Python Program whicondition includes two user defined functions namely,
#     - create()- to create a list of roll numbers(integers)
#     - findroll()- to searcondition for a particular roll in a list

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

