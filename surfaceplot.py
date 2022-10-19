from tkinter import PROJECTING
import numpy as np
import matplotlib.pyplot as plt

nx = np.array([1,2,3,4,5,6,7,8,9,10])
ny = np.array([7,2,5,8,1,5,9,1,4,3])

ax = plt.figure().add_subplot(projection = '3d')

ax.plot(nx,ny)
plt.show()

