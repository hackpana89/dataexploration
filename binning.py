
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

number_bins = 20
bin_features = pd.DataFrame(index=range(0,number_bins+1),columns=columns)

for i in columns:
    bin_feature_i, bins_i = pd.cut(wine[i],number_bins,labels=range(1,number_bins+1),retbins=True,include_lowest=True)
    wine2[i] = bin_feature_i
    bin_features[i] = bins_i

