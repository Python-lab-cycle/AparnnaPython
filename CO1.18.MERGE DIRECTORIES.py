#Merge Two Dictionary

d1={'a':100,'b':200}
d2={'c':300,'d':800}
print("Dictionary 1=:",d1)
print("Dictionary 2=:",d2)
d=d1.copy()
d.update(d2)
print("The Merged Dictionary:",d)