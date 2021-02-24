import pandas as pd 
import pickle
import os

with open('sp500_tickers.pickle','rb') as f:
    tickers=pickle.load(f)
main_df=pd.DataFrame()
for count,i in enumerate(tickers):
    if not os.path.exists('stock_dfs/{}.csv'.format(i)):
        break
    df=pd.read_csv('stock_dfs/{}.csv'.format(i))
    df.set_index('Date',inplace=True)
    df.drop(['Close','High','Volume','Open','Low'],1,inplace=True)
    df.rename(columns={'Adj Close':i},inplace=True)
    if main_df.empty:
        main_df=df
    else:
        main_df=main_df.join(df,how="outer")
    print("Merged {}".format(count))
print(main_df.head())
main_df.to_csv('stock_dfs/full_list.csv')