

n = int(input("Enter the Limit: \n"))

a = 0 #first number
b = 1 # second number

if n == 1:
    print(a)
else:
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


