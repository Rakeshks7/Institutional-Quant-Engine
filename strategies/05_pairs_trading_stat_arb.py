import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

tickers = ['HDFCBANK.NS', 'ICICIBANK.NS']
data = yf.download(tickers, start="2022-01-01", end="2024-01-01")['Close'] 

data = data.dropna()
stock_a = data['HDFCBANK.NS']
stock_b = data['ICICIBANK.NS']

score, pvalue, _ = coint(stock_a, stock_b)

print(f"Cointegration P-Value: {pvalue:.5f}")
if pvalue < 0.05:
    print("✅ SUCCESS: The pair is Cointegrated! The rubber band exists.")
else:
    print("❌ FAILURE: The pair is NOT Cointegrated. Do not trade this.")

x = sm.add_constant(stock_b)
result = sm.OLS(stock_a, x).fit()
hedge_ratio = result.params['ICICIBANK.NS']
print(f"Hedge Ratio: {hedge_ratio:.3f} (For every 1 HDFC, Short {hedge_ratio:.3f} ICICI)")

spread = stock_a - (hedge_ratio * stock_b)

z_score = (spread - spread.mean()) / spread.std()

plt.figure(figsize=(12, 6))
z_score.plot(label='Z-Score (The Rubber Band)')

plt.axhline(2.0, color='red', linestyle='--', label='Sell Zone (+2 Sigma)')
plt.axhline(-2.0, color='green', linestyle='--', label='Buy Zone (-2 Sigma)')
plt.axhline(0, color='black', linestyle='-', label='Mean (Exit)')

plt.title('Statistical Arbitrage Signal: HDFC vs ICICI')
plt.legend()
plt.show()