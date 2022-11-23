# 3. ILLUSTRATION OF MODULE PROGRAMMING
Create a package named "mymodule" containing three modules cube,
sphere and cylinder to find the surface area and volume of these shapes.
Later, import these modules into the main program and invoke the functions 
as a menu-driven program.

## Source Code
```py
import mymodule

while True:
    print("=============================================")
    print("What would you like to do?")
    print("""
    [1] Find surface area and volume of Cube
    [2] Find surface area and volume of Sphere
    [3] Find surface area and volume of Cylinder
    [4] Exit
    """)

    ch = input("Enter your choice[1/2/3/4]: ")

    if ch == "1":
        s = int(input("Enter side of Cube: "))
        mymodule.Cube(s)
    
    elif ch == "2":
        r = int(input("Enter radius of Sphere: "))
        mymodule.Sphere(r)

    elif ch == "3":
        r = int(input("Enter radius of Cylinder: "))
        h= int(input("Enter height of Cylinder: "))
        mymodule.Cylinder(r, h)

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

    [1] Find surface area and volume of Cube    
    [2] Find surface area and volume of Sphere  
    [3] Find surface area and volume of Cylinder
    [4] Exit
    
Enter your choice[1/2/3/4]: 1
Enter side of Cube: 2
Surface area of the Cube is 24
Volume of the Cube is 8
=============================================
What would you like to do?

    [1] Find surface area and volume of Cube
    [2] Find surface area and volume of Sphere
    [3] Find surface area and volume of Cylinder
    [4] Exit

Enter your choice[1/2/3/4]: 2
Enter radius of Sphere: 2
Surface area of the Sphere is 50.26548245743669
Volume of the Sphere is 33.510321638291124
=============================================
What would you like to do?

    [1] Find surface area and volume of Cube
    [2] Find surface area and volume of Sphere
    [3] Find surface area and volume of Cylinder
    [4] Exit

Enter your choice[1/2/3/4]: 3
Enter radius of Cylinder: 2
Enter height of Cylinder: 3
Surface area of the Cylinder is 62.83185307179586
Volume of the Cylinder is 37.69911184307752
=============================================
What would you like to do?

    [1] Find surface area and volume of Cube
    [2] Find surface area and volume of Sphere
    [3] Find surface area and volume of Cylinder
    [4] Exit

Enter your choice[1/2/3/4]: 4
[ Exiting ]
```
