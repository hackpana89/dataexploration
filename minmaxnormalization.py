import pandas as pd
import numpy as np

column_names = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
              'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
              'Color intensity','Hue','Diluted wines','Proline']

wine = pd.read_csv('wine.csv',names=column_names)