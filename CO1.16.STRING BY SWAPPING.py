# Create a single string separated with space from two strings by swapping the character at position 1.


a = input("Enter the value:\n")
b = input("Enter the another value:\n")
x = a[0:2]
a = a.replace(a[0:2], b[0:2])
b = b.replace(b[0:2], x)
print(a, b)
