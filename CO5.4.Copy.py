import csv
with open('employee1.csv',newline='')as csvfile1: data=csv.DictReader(csvfile1)
print("empno empname")
print("	")
for row in data :
print(row["Emp No"],row["Emp Name"])
