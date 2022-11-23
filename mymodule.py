from math import pi

def Cube(s):
    area = (s*s) * 6
    volume = s**3
    print("Surface area of the Cube is", area)
    print("Volume of the Cube is", volume)

def Sphere(r):
    area = 4*pi*(r**2)
    volume = (4/3)*pi*(r**3)
    print("Surface area of the Sphere is", area)
    print("Volume of the Sphere is", volume)

def Cylinder(r, h):
    area = (2*pi*(r**2)) + (2*pi*r*h)
    volume = pi*(r**2)*h
    print("Surface area of the Cylinder is", area)
    print("Volume of the Cylinder is", volume)
