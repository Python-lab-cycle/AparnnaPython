line="Blackpink in your area"
f1=open("text5.txt","w")
f1.write(line)
f1.close()

f1=open("text5.txt","r")
line=f1.read()
print("line",line)
f1.close()
