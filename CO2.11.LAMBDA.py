
import math

rectangle_area = lambda l, h : l*h
circle_area = lambda r: math.pi*r*r
triangle_area= lambda b,h:0.5*b*h

print("Area of Rectangle (30,20) is:", rectangle_area(30,20))
print("Area of circle (15) is:", circle_area(15))
print("Area of triangle (15) is:", triangle_area(15,15))