import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([7,2,5,8,1,5,9,1,4,3])

z =np.array ([4,3,9,5,1,4,0,2,7,2])
q= np.array([9,3,8,1,6,3,7,5,7,8])

plt.bar(x,y)
plt.bar(z,q)
plt.xticks()
plt.legend()
plt.show()