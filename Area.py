from Graphics.RectFunction import*
from Graphics.CircleFunction import *
#from DGraphics.SphereFunctions import *
#from DGraphics.CuboidFunctions import *

l=int(input("enter l:"))
b=int(input("enter b:"))

print("area = ",rectarea(l,b))
print("Perimeter =", rectperimeter(l,b))

r = int(input("enter the radius of a circle:"))
print("Circle area = ", ciclearea(r))
print("Circle Perimeter =", circleperimeter(r))

"""r = int(input("enter radius of Sphere:"))
print("Circle area = ", Spherearea(r))
print("Circle Perimeter =", Sphereperimeter(r)"""

"""a=int(input("Enter a side length :"))
print("Cube Area= ",cubearea(a))
h=int(input("enter l:"))
print("Cube Perimeter=",cubeperimeter(l,b,h))
"""