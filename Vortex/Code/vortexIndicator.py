import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as m

path = '/Users/hanya/Documents/01_Work/01_Projects/Fitztroy/'
# df01 = pd.read_csv("USDEUR_daily_2014.csv")
# df02 = pd.read_csv("USDEUR_daily_2015.csv")
# df03 = pd.read_csv("USDEUR_daily_2016.csv")
df = pd.read_csv("SPY_daily_1415.csv")
df2 = pd.read_csv("SPY_daily_2016.csv")
frames = [df, df2]
# frames = [df01, df02, df03]
df = pd.concat(frames).reset_index(drop=True)
n = df.shape[0]

lWindow = 14
VMp = np.abs(df['High']-df['Low'].shift(1))
VMn = np.abs(df['Low']-df['High'].shift(1))
VMp14 = VMp.rolling(window=lWindow, center=False).sum()
VMn14 = VMn.rolling(window=lWindow, center=False).sum()
TR = np.maximum(df['High']-df['Low'], np.abs(df['High']-df['Close'].shift(1)))
TR = np.maximum(TR, np.abs(df['Low']-df['Close'].shift(1)))
TR14 = TR.rolling(window=lWindow, center=False).sum()
VI14p = VMp14/TR14
VI14n = VMn14/TR14

# f, axarr = plt.subplots(2, sharex=True)
# axarr[0].plot(VMp)
# axarr[0].plot(VMn)
# axarr[1].plot(df['Close'])

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(VMp14)
axarr[0].plot(VMn14)
axarr[1].plot(df['Close'])

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(TR)
axarr[1].plot(TR14)

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(VI14p)
axarr[0].plot(VI14n)
axarr[1].plot(df['Close'])


# plt.figure()
# plt.plot(VI14n)



