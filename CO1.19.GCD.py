# GCD OF 2 NUMBERS

a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("The Gcd of Given Number is", a, "and", b, "is:", gcd)
