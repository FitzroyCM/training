# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:22:05 2017

@author: GEORGES
"""

# forTraining.py

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\pythonTesting\\individual_days\\SPY\\'

def f(x):
    t = int(''.join(x[0:8].split(':')))
    return 93000 <= t < 160000

list0 = [i for i in os.listdir(path) if i.endswith('.txt') and i[2:4] in ['14', '15']]

for i in list0:
    df = pd.read_csv(path + i)
    df2 = df[df['Time'].map(f)]
    if i == '2014-01-02.txt':
        df0 = df2
    else:
        df0 = df0.append(df2)

def g(df):
    return pd.Series({'Close': df['Price'].iloc[-1], 'Open': df['Price'].iloc[0], 'High': max(df['Price']), 'Low': min(df['Price'])})

df1 = df0.groupby(['Date']).apply(g).reset_index()
dt1 = pd.to_datetime(df1['Date'], format="%d/%m/%Y")
df1['dt'] = dt1
df1 = df1.sort(['dt']).reset_index(drop=True)

plt.plot(df1['Close'])

df1.to_csv('SPY_daily_1415.csv', index=False)




## USDEUR
path = 'C:\\pythonTesting\\individual_days\\EURUSD\\'

def g(df):
    return pd.Series({'Close': df['Price'].iloc[-1], 'Open': df['Price'].iloc[0], 'High': max(df['Price']), 'Low': min(df['Price'])})

for j in range(2014, 2017):
    list0 = [i for i in os.listdir(path) if i.startswith(str(j))]
    for i in list0:
        df = pd.read_csv(path + i)
        if i == list0[0]:
            df0 = df
        else:
            df0 = df0.append(df)

df0 = df0.reset_index(drop=True)
Price = (df0['bid'] + df0['ask'])/2
df0['Price'] = Price
dt1 = pd.to_datetime(df0['time'], format="%Y%m%d %H:%M:%S.%f", errors='coerce')
df0['date'] = dt1.dt.date
df1 = df0.groupby(['date']).apply(g).reset_index()
df1.to_csv('USDEUR_daily_' + str(j) + '.csv', index=False)

