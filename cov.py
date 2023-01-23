import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Maths = [45, 37, 42, 35, 39]
English = [38, 31, 26, 28, 33]
Science = [10, 15, 17, 21, 12]

data = np.array([Maths, English, Science])

cov_matrix = np.cov(data, bias=True)
print(cov_matrix)
sns.heatmap(cov_matrix, annot=True, fmt='g', xticklabels=data, yticklabels=data, cmap = 'crest')
plt.show()