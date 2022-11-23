# 1. ILLUSTRATION OF FUNCTION PROGRAMMING
Develop a menu-driven program in Python using user defined functions to find the
area of different shapes (Circle, Square and Rectangle).

## Source Code
```py
from math import pi

def AreaSquare(s):
    area = s * s
    return area

def AreaRectangle(l, b):
    area = l * b
    return area

def AreaCircle(r):
    area = pi * (r**2)
    return area

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Find the area of a Rectangle
    [2] Find the area of a Square
    [3] Find the area of a Circle
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        l = int(input("Enter length of Rectangle: "))
        b = int(input("Enter breadth of Rectangle: "))
        area = AreaRectangle(l, b)
        print("Area of the Rectangle is", area)
    
    elif ch == "2":
        s = int(input("Enter side of Square: "))
        area = AreaSquare(s)
        print("Area of the Square is", area)

    elif ch == "3":
        s = int(input("Enter radius of Circle: "))
        area = AreaCircle(s)
        print("Area of the Circle is", area)

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

    [1] Find the area of a Rectangle
    [2] Find the area of a Square
    [3] Find the area of a Circle
    [4] Exit

Enter your choice[1/2/3/4]: 1
Enter length of Rectangle: 2
Enter breadth of Rectangle: 3
Area of the Rectangle is 6
=============================================
What would you like to do?

    [1] Find the area of a Rectangle
    [2] Find the area of a Square
    [3] Find the area of a Circle
    [4] Exit
    
Enter your choice[1/2/3/4]: 2
Enter side of Square: 3
Area of the Square is 9
=============================================
What would you like to do?

    [1] Find the area of a Rectangle
    [2] Find the area of a Square
    [3] Find the area of a Circle
    [4] Exit

Enter your choice[1/2/3/4]: 3
Enter radius of Circle: 2
Area of the Circle is 12.566370614359172
=============================================
What would you like to do?

    [1] Find the area of a Rectangle
    [2] Find the area of a Square
    [3] Find the area of a Circle
    [4] Exit

Enter your choice[1/2/3/4]: 4
[ Exiting ]
```
