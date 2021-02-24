import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import pickle
from collections import Counter
from split_data import split_data,get_dict
from KNN import knn,get_accuracy

def process_data_for_labels(ticker):
    hm_days=7
    df=pd.read_csv('stock_dfs/full_list.csv',index_col=0)
    tickers=df.columns.values.tolist()
    for i in range(1,hm_days+1):
        df['{}_{}_days'.format(ticker,i)]=(df[ticker].shift(-i)-df[ticker])/df[ticker]
    df.fillna(0,inplace=True)
    return tickers,df

def buy_sell_hold(*args):
    cols=[c for c in args]
    requirement=0.02
    for col in cols:
        if col>requirement:
            return 1     #BUY
        if col<-requirement:
            return -1    #SELL  
    return 0     #HOLD

def extract_labels(ticker):
    tickers,df=process_data_for_labels(ticker)
    df['{}_target'.format(ticker)]=list(map(buy_sell_hold,df['{}_1_days'.format(ticker)],
    df['{}_2_days'.format(ticker)],
    df['{}_3_days'.format(ticker)],
    df['{}_4_days'.format(ticker)],
    df['{}_5_days'.format(ticker)],
    df['{}_6_days'.format(ticker)],
    df['{}_7_days'.format(ticker)]))
    
    values=df['{}_target'.format(ticker)].values.tolist()
    dictionary=Counter(values)
    print('Data Spread: ',dictionary)
    df.fillna(0,inplace=True)
    df.replace([np.inf,-np.inf],np.nan,inplace=True)
    df.dropna(inplace=True)

    df_vals=df[[ticker for ticker in tickers]].pct_change()
    df_vals.replace([np.inf,-np.inf],0,inplace=True)
    df_vals.fillna(0,inplace=True) 
    X=df_vals.values
    y=df['{}_target'.format(ticker)].values
    return X,y,df

def do_ML(ticker):
    X,y,df=extract_labels(ticker)
    x=[]
    for i in range(len(X)):
        a=list(X[i])
        a.append(y[i])
        x.append(a)
        a=[]
    X_train=x[:-int(len(x)*0.25)]
    X_test=x[-int(len(x)*0.25):]
    print("Accuracy: ",get_accuracy(X_test,1,-1,get_dict(X_train,1,-1),7)[0])

do_ML("A")
    

   

    
     
      

  