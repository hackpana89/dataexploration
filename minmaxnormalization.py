

import pandas as pd
import numpy as np
from sqlalchemy import column

column_names = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
              'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
              'Color intensity','Hue','Diluted wines','Proline']

wine = pd.read_csv('wine.csv',names=column_names)

wine_class = wine['class']
del wine['class']

wine2 =  wine.copy()
columns = wine2.columns
min_max_features = pd.DataFrame(index = ['min','max'],columns=columns)

for i in columns:
    min_value = wine2[i].min()
    max_value = wine2[i].max()

    #it is important to store the min_max values as they will be used later for normalization of the new data before classification
    min_max_features.loc['min',i] = min_value
    min_max_features.loc['max',i] = max_value

    wine2[i] = [(x - min_value) / (max_value - min_value) for x in wine2[i]]



