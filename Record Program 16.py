# 16. ILLUSTRATION OF STACK PROGRAMMING USING LIST OF PRODUCTS – III
# Develop a program to implement the following stack operations in python
# using list of product names.
#     1. Push an item name to the stack(the products whose name starts with b/B)
#     2. Pop item name from the stack
#     3. Display the stack
#     4. Exit

stack = [] # stack is a global variable

def push(name):
    if name[0] in "Bb":
        stack.append(name)
        print(name, "was added to the stack")
    else:
        print("Product name does not start with 'b'")

def pop():
    if stack != []:
        product = stack.pop()
        print(product, "was popped from the stack")
    else:
        print("Stack Underflow")
        print("There are no items in the stack")
        
def showStack():
    print("--------------------")
    for product in stack:
        print(product)
    print("--------------------")



while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Push a product to the stack (if it's name starts with 'b')
    [2] Pop a product from the stack
    [3] Display the list of products
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        name = input("Enter product name: ")
        push(name)
    
    elif ch == "2":
        pop()

    elif ch == "3":
        showStack()

    elif ch == "4":
        print("[ Exiting ]") # Break from the loop to exit
        break

    else:
        print("[ Invalid Choice ]") # In case user inputs a choice that was not defined


