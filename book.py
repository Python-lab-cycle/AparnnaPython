class publisher:
     def __init__(self,pname):
         self.pname=name
     def display(self):
         print("Name",self.pname)

class Book(publisher):
     def __init__(self,pname,bname,title):
       self.pname=pname
       self.bname=bname
       self.title=title

     def display(self):
        print("name",selfpname)
        print("bname",self.bname)
        print("title",se.title)

class python(Book):
     def __init__(self,pname,bname,title,page,price):
         self.pname=pname
         self.bname=bname
         self.title=title
         self.page=page
         self.price=price

     def display(self):
        print("pname",self.pname)
        print("bname",self.bname)
        print("title",self.title)
        print("page",self.page)
        print("price",self.price)



n=input("enter the publisher Name")
b=input("Enter the Book")
t=input("Enter the Title")
p=int(input("Enter pages"))
pr = int(input("Enter Price"))
obj = python(n,b,t,p,pr)
obj.display()
       
