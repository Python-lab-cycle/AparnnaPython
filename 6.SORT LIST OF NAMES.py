# Store a list of first names. Count the occurrences of ‘a’ within the list.

astr = input("Enter the String:\n")
char = input("Enter the character:\n")
print("Given String:\n", astr)
print("Given Character:\n", char)
res = 0
for i in range(len(astr)):
    if astr[i] == char:
        res = res + 1
print("Number of time character is present in string:\n", res)
