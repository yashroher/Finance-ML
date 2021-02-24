import pandas_datareader.data as web
import os
import pickle 
import pandas as pd 
import datetime as dt

if not os.path.exists('stock_dfs'):
    os.makedirs('stock_dfs')
with open('sp500_tickers.pickle','rb') as f:
    tickle=pickle.load(f)
print(tickle)
start=dt.datetime(2010,1,1)
end=dt.datetime.today()
for i in tickle:
    if not os.path.exists('stock_dfs/{}.csv'.format(i)):
        data=web.DataReader(i,'yahoo',start,end)
        data.to_csv('stock_dfs/{}.csv'.format(i))
        print("Downloaded {}".format(i))
    else:
        print("The file already exists")

