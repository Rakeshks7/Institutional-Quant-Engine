import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['TATAMOTORS.NS', 'HINDUNILVR.NS', 'TITAN.NS', 'SUNPHARMA.NS']
data = yf.download(tickers, start="2022-01-01", end="2024-01-01")['Close'] 
returns = data.pct_change().dropna()

num_portfolios = 5000
results = np.zeros((3, num_portfolios)) 

for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights) 

    p_return = np.sum(returns.mean() * weights) * 252 
    p_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

    results[0,i] = p_return
    results[1,i] = p_volatility
    results[2,i] = p_return / p_volatility 

max_sharpe_idx = np.argmax(results[2])
best_return = results[0, max_sharpe_idx]
best_vol = results[1, max_sharpe_idx]

print(f"--- OPTIMAL PORTFOLIO ---")
print(f"Max Sharpe Ratio: {results[2, max_sharpe_idx]:.2f}")
print(f"Expected Annual Return: {best_return*100:.2f}%")
print(f"Expected Volatility:    {best_vol*100:.2f}%")

plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', alpha=0.5)
plt.colorbar(label='Sharpe Ratio')
plt.scatter(best_vol, best_return, c='red', s=50, marker='*', label='Max Sharpe')
plt.xlabel('Risk (Volatility)')
plt.ylabel('Return')
plt.title('Efficient Frontier (Portfolio Optimization)')
plt.legend()
plt.show()