


class area:
    def __init__(self,m1,m2): #initialization
        self.l=m1
        self.b=m2
    def __gt__(self,other): #compairing the two objects
        r1=self.l*self.b
        r2=other.l*other.b
        if(r1>r2):
            return True
        else:
            return False
a=int(input("Enter length of first triangle:"))
b=int(input("Enter breadth of first triangle:"))
c=int(input("enter length of second triangle:"))
d=int(input("Enter breadth of second triangle:"))
s1=area(a,b)
s2=area(c,d)
if(s1>s2):
    print("Area of rect1 is greater:")
else:
    print("Area of rect2 is greater:")








0.
