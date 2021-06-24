#Python program to display calendar
month=int(input("enter month:"))
year=int(input('enter year:'))
date=int(input('enter date:'))
import calendar
print(calendar.month(year , month, date)) 