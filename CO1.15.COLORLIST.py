#  Print out all colors from color-list1 not contained in color-list2

colorlist1 = set(["White", "Black", "Red"])
colorlist2 = set(["Red", "Green"])

print(colorlist1.difference(colorlist2))
