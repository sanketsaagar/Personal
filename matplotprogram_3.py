import numpy as np
import matplotlib.pyplot as plt

x= np.array([2,4,6,8,10,12,14,16,18,20])
y= np.array([10,20,30,40,50,60,70,80,90,100])
mycolour = ["Red", "Yellow", "Green", "Blue"]

plt.scatter(x,y, c=mycolour, cmap= 'Greens')
plt.colorbar()
plt.show()