# 15. ILLUSTRATION OF STACK PROGRAMMING USING LIST OF VOTERS – II
# Develop a python program to implement the following operations on a stack
# containing voters list details (ID,NAME,AGE)as per user’s choice.
#     1. Push a voter record to the stack
#     2. Pop a voter record from the stack
#     3. Display the list of voters
#     4. Exit

stack = [] # stack is a global variable

def push(record):
    stack.append(record)
    print(record[1], "was added to the stack")

def pop():
    if stack != []:
        voter = stack.pop()
        print(voter[1], "was popped from the stack")
    else:
        print("Stack Underflow")
        print("There are no items in the stack")
        
def showStack():
    for voter in stack:
        print("--------------------")
        print("ID   :", voter[0])
        print("Name :", voter[1])
        print("Age  :", voter[2])
        print("--------------------")


while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Push a voter record to the stack
    [2] Pop a voter record from the stack
    [3] Display the list of voters
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        ID = int(input("Enter Voter ID: "))
        Name = input("Enter Voter Name: ")
        Age = int(input("Enter Voter Age: "))
        push([ID, Name, Age])
    
    elif ch == "2":
        pop()

    elif ch == "3":
        showStack()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined


