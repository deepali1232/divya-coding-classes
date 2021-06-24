#Python Program to Check Leap Year
year=int(input('enter the year:'))
if year%400==0:
    print('it is leap year.')
elif year%4==0:
    print('it is also a leap year.')
else:
    print('it is not a leap year.')