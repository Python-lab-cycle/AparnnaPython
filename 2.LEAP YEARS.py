# Display future leap years from current year to a final year entered by user.

print("______Print Leap Year between two given years_____")
startyear=int(input("Enter the Start Year:"))
endyear=int(input("Enter the End Year:"))
for year in range(startyear,endyear):
    if ((year % 4 == 0) and (year % 100!=0) or (year % 400==0)):
          print(year)