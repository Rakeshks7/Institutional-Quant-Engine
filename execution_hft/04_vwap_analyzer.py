import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "TCS.NS"
data = yf.download(ticker, period="5d", interval="1m")

def calculate_vwap(df):
    df['Typical_Price'] = (df[('High', ticker)] + df[('Low', ticker)] + df[('Close', ticker)]) / 3

    df['VP'] = df['Typical_Price'] * df[('Volume', ticker)]

    df['Cumulative_VP'] = df.groupby(df.index.date)['VP'].cumsum()
    df['Cumulative_Volume'] = df[('Volume', ticker)].groupby(df.index.date).cumsum()

    df['VWAP'] = df['Cumulative_VP'] / df['Cumulative_Volume']
    return df

data = calculate_vwap(data)

plt.figure(figsize=(12, 6))

last_day = data.index[-1].date()
day_data = data[data.index.date == last_day]

plt.plot(day_data.index, day_data[('Close', ticker)], label='TCS Price', color='black', alpha=0.6)
plt.plot(day_data.index, day_data['VWAP'], label='VWAP (Institutional Line)', color='blue', linewidth=2)

plt.title(f'TCS Intraday Price vs. VWAP ({last_day})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()