"""
THE PATTERN
1
2 4
3 6 9
4 8 12 16


"""

rows=5
for i in range(rows):
    for j in range(1 ,  i+1):
        print(i*j,end="  "  )
    print()