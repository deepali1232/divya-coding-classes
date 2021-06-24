#Python program to find the area of a triangle
a=float(input('enter a value:'))
b=float(input('enter b value:'))
c=float(input('enter c value:'))
s=(a+b+c)/2
print('semiperimeter is {}'.format(s))
area=(s*(s-a)*(s-b)*(s-c))/2
print('area is {}'.format(area))