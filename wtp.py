# analysis of wilingness to pay for plant based menu items

import pandas as pd
import hvplot.pandas
import holoviews as hv

prices = pd.read_csv('C:/Users/socie/OneDrive/Documents/thesis 1 and 2/thesis 2/data/price1.csv',sep=';', engine='python')

prices1 = prices.drop(['index','Frame'], axis =1, inplace=True)

prices2 = pd.read_csv('C:/Users/socie/OneDrive/Documents/thesis 1 and 2/thesis 2/data/price2.csv',sep=';', engine='python')

prices3 = prices2.drop(['index','Frame'], axis =1, inplace=True)

prices4 = pd.read_csv('C:/Users/socie/OneDrive/Documents/thesis 1 and 2/thesis 2/data/price3.csv',sep=';', engine='python')

prices5 = prices4.drop(['index','Frame'], axis =1, inplace=True)


df = pd.DataFrame(prices)
df1 = pd.DataFrame(prices2)
df2 = pd.DataFrame(prices4)


print(df)
print(df1)
print(df2)

def price_sensitivity_meter(df, interpolate=False):
    # convert data from wide to long
    # calculate frequency of each price for each group
    df1 = (df[['Too Cheap', 'Cheap', 'Expensive', 'Too Expensive']]
             .unstack()
             .reset_index()
             .rename(columns = {'level_0':'label', 0: 'prices'})[['label','prices']]
             .groupby(['label','prices'])
             .size()
             .reset_index()
             .rename(columns = {0: 'frequency'})
            )
    # calculate cumsum percentages
    df1['cumsum'] = df1.groupby(['label'])['frequency'].cumsum()
    df1['sum'] = df1.groupby(['label'])['frequency'].transform('sum')
    df1['percentage'] = 100*df1['cumsum']/df1['sum']
    # convert data from long back to wide
    df2 = df1.pivot_table('percentage', 'prices', 'label')
    
    # take linear values in missing values
    if interpolate:
        df3 = df2.interpolate().fillna(0)
        df3['Too Cheap'] = 100 - df3['Too Cheap']
        df3['Cheap'] = 100 - df3['Cheap']
        plot = df3.hvplot(x='prices', 
                          y=['Too Cheap', 'Cheap', 'Expensive', 'Too Expensive'],
                          ylabel = 'Percentage',
                          height=400,
                          color=['green','lightgreen','lightpink','crimson']
                              ).opts(legend_position='bottom')
    
    # forward fill 
    else: 
        df3 = df2.ffill().fillna(0)
        
        df3['Too Cheap'] = 100 - df3['Too Cheap']
        df3['Cheap'] = 100 - df3['Cheap']
        plot = df3.hvplot.step(x='prices', 
                               y=['Too Cheap', 'Cheap', 'Expensive', 'Too Expensive'],
                               where='post',
                               ylabel = 'Percentage',
                               height=400,
                               color=['green','lightgreen','lightpink','crimson']
                              ).opts(legend_position='bottom')
    df3['optimal_diff'] = (df3['Too Cheap'] - df3['Too Expensive'])
    df3['left_diff'] = (df3['Too Cheap'] - df3['Expensive'])
    df3['right_diff'] = (df3['Too Expensive'] - df3['Cheap'])
    optimal = df3[df3['optimal_diff']<=0].index[0]
    lower_bound = df3[df3['left_diff']<=0].index[0]
    upper_bound = df3[df3['right_diff']>=0].index[0]
    

    optimal_line = hv.VLine(optimal).opts(color='blue', line_dash='dashed', line_width=0.4)

    lower_line = hv.VLine(lower_bound).opts(color='grey', line_dash='dashed', line_width=0.4)
    upper_line = hv.VLine(upper_bound).opts(color='grey', line_dash='dashed', line_width=0.4)

   
    print(f'Optimal Price: ${optimal}')
    print(f'Acceptable Price Range: ${lower_bound} to ${upper_bound}') 
    

    return plot * lower_line * optimal_line * upper_line
