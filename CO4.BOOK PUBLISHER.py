class publisher:
    def __init___(self,pname):
        self.pname=pname
    def display(self):
        print("Name",self.name)
class book(publisher):
    def __init__(self,pname,bname,title):
        self.pname=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("Name",self.pname)
        print("bname",self.bname)
        print("Title",self.tname)
class python(book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("Publisher name:",self.pname)
        print("book:",self.bname)
        print("title:",self.title)
        print("page:",self.page)
        print("price:",self.price)
n=input("Enter publisher:")
b=input("Enter book:")
t=input("Enter title:")
p=int(input("Enter pages:"))
pr=int(input("Enter price:"))
obj=python(n,b,t,p,pr)
obj.display()