li=[1,2,3,4,5]
from functools import reduce
l2=reduce(lambda x,y:x+y,li)
print(l2)