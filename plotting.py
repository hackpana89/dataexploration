#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

column_names = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
              'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
              'Color intensity','Hue','Diluted wines','Proline']

wine = pd.read_csv('wine.csv',names=column_names)

fig, ax = plt.subplots()

data_array = np.array(wine['Alcohol'])
ax.hist(data_array,bins=10)
# %%
