import numpy as np
import matplotlib.pyplot as plt

y= np.array([20,30,40,10])
fruit = {"Apple", "Banana", "Cherry", "Orange"}
mycolour = ["Red", "Yellow", "Green", "Blue"]
myexplode = [0, 0.1,0,0]
plt.pie(y, labels = fruit,explode = myexplode,shadow = True, colors= mycolour, autopct= '%.1f%%')
plt.legend(title = fruit)
plt.show()