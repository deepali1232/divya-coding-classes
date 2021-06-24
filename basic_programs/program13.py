a=100                                           #if condition
b=20
if b>a:
    print('b is greater than a')
else:                                           #else
    print("a is greater than b")
a=20
b=30
c=40
if a>b & a>c:
    print("a is the greatest")
elif b>a & b>c:                                                     #elif
    print("b is greater")
else:
    print("c is greater")
#if with tuple
t1=(1,2,'sparta')
if 2 in t1:
    print("present")
else:
    print('not present')

#if with list
l1=['a','b','c']
if l1[0]=='a':
    l1[0]='d'
print(l1)
#if with dict
d1={'pen':5,"pencil":2,'bag':500}
if d1['bag']==500:
    d1['bag']=d1['bag']+20
print(d1)

