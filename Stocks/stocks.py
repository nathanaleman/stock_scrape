import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2020, 4, 1)
end = dt.datetime(2020, 4, 30)

df = web.DataReader('TSLA', 'yahoo', start, end)
# df.to_csv('tsla.csv')
# df = pd.read_csv('tsl.csv')
# df['Adj Close'].plot()
#df.plot()
#plt.show()
print(df)
