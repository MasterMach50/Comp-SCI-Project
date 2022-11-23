# 3. ILLUSTRATION OF MODULE PROGRAMMING
# Create a package named "mymodule" containing three modules cube,
# sphere and cylinder to find the surface area and volume of these shapes.
# Later, import these modules into the main program and invoke the functions 
# as a menu-driven program.

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
