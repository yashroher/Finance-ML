import pandas_datareader.data as web
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.dates as mpdates
from mpl_finance import candlestick_ohlc
from matplotlib import style
import datetime as dt

style.use('ggplot')

start=dt.datetime(2020,1,1)
end=dt.datetime.today()

data=web.DataReader('TSLA','yahoo',start,end)
#print(data.head(6))

data['100ma']=data['Adj Close'].rolling(100).mean()
#print(data.tail(6))

data_ohlc=data['Adj Close'].resample('10D').ohlc()
#print(data_ohlc)
data_volume=data['Volume'].resample('10D').sum()

data_ohlc.reset_index(inplace=True)
data_ohlc['Date']=list(map(mpdates.date2num,data_ohlc['Date']))
print(data_ohlc)
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
ax1.xaxis_date()
ax2.fill_between(data_volume.index.map(mpdates.date2num),data_volume.values)
candlestick_ohlc(ax1,data_ohlc.values,width=2,colorup='g')
plt.show()