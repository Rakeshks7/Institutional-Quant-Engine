import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = "^NSEI"
data = yf.download(ticker, start="2015-01-01", end="2024-01-01")
data = data.dropna()

data['SMA_50'] = data[('Close', ticker)].rolling(window=50).mean()
data['SMA_200'] = data[('Close', ticker)].rolling(window=200).mean()

data['Signal'] = np.where(data['SMA_50'] > data['SMA_200'], 1, 0)

data['Market_Returns'] = data[('Close', ticker)].pct_change()
data['Strategy_Returns'] = data['Signal'].shift(1) * data['Market_Returns']

data['Cumulative_Market'] = (1 + data['Market_Returns']).cumprod()
data['Cumulative_Strategy'] = (1 + data['Strategy_Returns']).cumprod()

data['Running_Max'] = data['Cumulative_Strategy'].cummax()

data['Drawdown'] = (data['Cumulative_Strategy'] / data['Running_Max']) - 1

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(data['Cumulative_Market'], label='Nifty 50 (Buy & Hold)', color='gray', alpha=0.6)
ax1.plot(data['Cumulative_Strategy'], label='SMA 50/200 Strategy', color='blue')
ax1.set_title('Strategy vs. Market Performance')
ax1.set_ylabel('Growth of ₹1')
ax1.legend()

ax2.fill_between(data.index, data['Drawdown'], 0, color='red', alpha=0.3)
ax2.set_title('Drawdown (Risk: How much you are down from the peak)')
ax2.set_ylabel('Percentage Loss')
ax2.grid(True, alpha=0.3)

plt.show()

max_drawdown = data['Drawdown'].min()
total_return = data['Cumulative_Strategy'].iloc[-1] - 1

print(f"Total Return: {total_return*100:.2f}%")
print(f"Max Drawdown: {max_drawdown*100:.2f}% (Worst drop from peak)")