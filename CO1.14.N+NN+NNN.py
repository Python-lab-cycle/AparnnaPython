a=int(input("Enter a Number:\n"))

n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))

print(n1, "  ", n2, "  ", n3)
print("SUM=", (n1 + n2 + n3))
