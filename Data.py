import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates
import datetime
import pandas as pd
from mpl_finance import candlestick_ohlc
from matplotlib import style
style.use('ggplot')

start=datetime.datetime(2020,1,1)
end=datetime.datetime.today()

data=web.DataReader('TSLA','yahoo',start,end)
data['100ma']=data['Adj Close'].rolling(100).mean() #rolling average...

print(data.head(200))
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
ax2.bar(data.index,data['Volume'])
data_ohlc=data['Adj Close'].resample('10D').ohlc() #open,high,close,low of every 10 days
data_ohlc.reset_index(inplace=True)
data_ohlc['Date']=list(map(mpdates.date2num,data_ohlc['Date'])) 
candlestick_ohlc(ax1,data_ohlc.values,width=2,colorup='g')
data_volume=data['Volume'].resample('10D').sum() #Sum of the volume of all the days with diff of 10
  # Setting index to serial numbers #Milliseconds///
print(data_ohlc)
plt.show()