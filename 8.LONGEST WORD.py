# Accept a list of words and return length of longest word.


a = []
n = int(input("Enter the Number of element in list:\n"))
for x in range(0, n):
    element = input("Enter element" + str(x + 1) + ":")
    a.append(element)
max1 = len(a[0])
temp = a[0]
for i in a:
    if (len(i) > max1):
        max1 = len(i)
        temp = i
print("The Word with the longest length is:")
print(temp)
