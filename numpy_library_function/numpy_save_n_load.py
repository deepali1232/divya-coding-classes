import numpy as np
n1=np.array([1,2,3,4,5])
np.save('my_numpy',n1)
n2=np.load('my_numpy.npy')
print(n2)