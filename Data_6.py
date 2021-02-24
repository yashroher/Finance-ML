import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np

data=pd.read_csv('stock_dfs/full_list.csv',index_col=0)
data.fillna(0,inplace=True)
print(data.head(6))
fig=plt.figure()
data_corr=data.corr()  # Slope by applying linear regression
dp=data_corr.values
ax=fig.add_subplot(111)  
heatmap=ax.pcolor(dp,cmap=plt.cm.RdYlGn)
fig.colorbar(heatmap)
ax.set_xticks(np.arange(dp.shape[0])+0.5)
ax.set_yticks(np.arange(dp.shape[1])+0.5)
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.set_xticklabels(data_corr.columns)
ax.set_yticklabels(data_corr.index)
plt.xticks(rotation=90)
heatmap.set_clim(-1,1)
plt.tight_layout()
plt.show()
print(np.arange(dp.shape[0]))