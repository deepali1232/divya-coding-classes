#sets
s1={1,3.14,'sparta'}
print(s1)
print(type(s1))
s2={1,1,3.14,3.14}          #duplicates not allowed
print(s2)

#add element in a set
s1.add('hello')
print(s1)

#update multiple element
s1.update([10,20,30])
print(s1)

#remove an element
s1.remove(1)
print(s1)

#union of two sets
x={1,2,3,4,5,6}
y={4,2,3,4,5,3}
x.union(y)
print(x)

#intersection of two set
x={1,2,3,4,5,6}
y={4,2,3,4,5,3}
y.intersection(x)
print(y)
