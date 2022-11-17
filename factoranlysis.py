# factor analysis 

import pandas as pd
import sklearn.datasets
from factor_analyzer import FactorAnalyzer 
from factor_analyzer.factor_analyzer import calculate_kmo
import matplotlib.pyplot as plt
import pingouin as pg

df = pd.read_csv('C:/Users/socie/OneDrive/Documents/thesis 1 and 2/thesis 2/data/data qualitative.csv',sep=';', engine='python')

df.drop(['index', 'age', 'sex', 'no. people in houshold','Frame', '6','7','8','9','10','11','12'], axis=1, inplace=True)

df.dropna

kmo_all,kmo_model=calculate_kmo(df)
print(kmo_model)

fa = FactorAnalyzer(n_factors=1, rotation= None)

fa.fit(df)

loadings = fa.loadings_

print(loadings)

ev, v = fa.get_eigenvalues()

xvals = range(1, df.shape[1]+1)

plt.scatter(xvals, ev)
plt.plot(xvals, ev)
plt.title('Scree Plot')
plt.xlabel('factor')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

fa.get_communalities()

pg.cronbach_alpha(data=df)
