import csv
csv_col=['ID','Name','Country']
dict_data=[{'ID':1,'Name':'Alex','Country':'India'},
           {'ID':2,'Name':'Ben','Country':'USA'},
           {'ID':3,'Name':'Shri Ram','Country':'USA'},
           {'ID':4,'Name':'Minnu','Country':'CANADA'},
           {'ID':5,'Name':'jenny','Country':'CANADA'},
           {'ID':6,'Name':'Jisoo','Country':'CANADA'},
           {'ID':7,'Name':'Rose','Country':'CANADA'},]
try:
    with open("Names.csv",'w')as file1:
        writer1=csv.DictWriter(file1,fieldnames=csv_col)
        writer1.writeheader()
        for data1 in dict_data:
            writer1.writerow(data1)
except IOError:            
       print("I/O Error")
data1=csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
