# Accept a file name from user and print extension of that


a = input("Input the element:\n")
f_ext=a.split(".")
print("the extension of the file is :" +repr(f_ext[-1]))