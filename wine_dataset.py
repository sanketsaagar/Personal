import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
df = pd.read_csv("/kaggle/input/wineuci/Wine.csv")
df.head()