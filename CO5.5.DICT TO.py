import csv
csv_col=['ID','Name','Place']
dict_data=[{'ID':1,'Name':'Akhila','Place':'Kodanad'},
           {'ID':2,'Name':'Ramsina','Place':'Irumalappady'},
           {'ID':3,'Name':'Anjaly','Place':'Paingottur'},
           {'ID':4,'Name':'Aparna','Place':'Cheruvattur'},
           {'ID':5,'Name':'Nivya','Place':'Muvattupuzha'}]
try:
    with open("Names.csv","w") as file1:
        writer1=csv.DictWriter(file1,fieldnames=csv_col)
        writer1.writeheader()
        for data1 in dict_data:
            writer1.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
