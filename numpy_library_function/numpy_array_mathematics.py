import numpy as np
n1=np.array([10,20,30,40])
n2=np.array([30,40,60,90])
print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=0))       #add coloumn
print(np.sum([n1,n2],axis=1))       #add row