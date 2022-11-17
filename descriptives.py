# questionaire analysis for descriptive characteristics 

import pandas as pd
import numpy as np
import pingouin as pg
import matplotlib.pyplot as plt

df = pd.read_csv (r'C:\Users\socie\OneDrive\Documents\thesis 1 and 2\thesis 2\data\attitudes vegeterianism.csv',sep=';'  )
df4 = pd.read_csv (r'C:\Users\socie\OneDrive\Documents\thesis 1 and 2\thesis 2\data\data qualitative.csv',sep=';'  )

df1 = pd.DataFrame(df)

df1.drop(['index', 'age','sex'], axis=1, inplace=True)

df4.drop(['index', 'age', 'sex', 'no. people in houshold','5','8','9','10','11'], axis=1, inplace=True)


print(df1.describe())

pg.cronbach_alpha(data=df1)

df3 = pd.read_csv (r'C:\Users\socie\OneDrive\Documents\thesis 1 and 2\thesis 2\data\sensory data.csv',sep=';'  )


df2 = pd.DataFrame(df3)
df2.drop(['index'], axis=1, inplace=True)

print(df2.describe())

pg.cronbach_alpha(data=df2)
