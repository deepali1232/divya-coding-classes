import numpy as np
n1=np.array([10,20,30,40,50,60])
n2=np.array([30,40,60,90])
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))