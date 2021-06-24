#list
a = [1,2.14,'sing',67,83]
print(type(a))
print(len(a))

#extract first element from list
print(a[0])

#last elemnt from list
print(a[-1])

#sequence of elemnt
print(a[2:4])

#changing element at index
a[0]=89
print(a)
a[3]='divya'
print(a)

#add a new elemnet
a.append('deepali')
print(a)

#pop last element
a.pop()
print(a)

#insert element at specified index
b=[63,'divya','pinky']
print(b.insert(63,'divya'))

#reversiing elements of list
a.reverse()
print(a)

#sorting a list
x=[25,75,23,8,35]
x.sort()
print(x)

#concatenate list
x=[1,2,3,4,5]
y=[2,3,4,5,6]
z=x+y
print(z)

#repeatong elements of list
print(x*3+y)