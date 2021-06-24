                #tuple
t1 = (1,'a','true',3.14)
print(type(t1))
print(t1[0])

#extract last element
print(t1[-1])

#want middlle two element
print(t1[1:3])

#find len of tuple
print(len(t1))

#concatenate tuple
t2=(35,'divya','true')
t3=t1+t2+t1
print(t3)
print(len(t3))

#repeating tuple element
t4=('divya',1996 )
print(t4*4)

#repeating and concatenating
print(t2*2+t4)

#min value of tuple
c=(13,2,3,43,4)
print(min(c))
print(max(c))