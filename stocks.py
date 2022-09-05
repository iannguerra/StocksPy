import datetime as dt
from multiprocessing import connection
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web



style.use('ggplot')

start = dt.datetime(2022, 4, 4)
end = dt.datetime.now()


df = web.DataReader("TSLA", 'yahoo', start, end)
df.to_csv('tsla.csv')
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

print(df.head())