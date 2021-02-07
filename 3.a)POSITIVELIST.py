"""

3. List comprehensions:
(a) Generate positive list of numbers from a given list of integers
(b) Square of N numbers
(c) Form a list of vowels selected from a given word
(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

"""

list1 = [11, -21, 0, 45, 66, -93]
# iterating each number in list
for num in list1:
    # checking condition
    if num >= 0:
       print(num, end = " ")
