import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")['Close']
returns = data.pct_change().dropna()

weights = np.array([0.25, 0.25, 0.25, 0.25])
portfolio_returns = returns.dot(weights)

confidence_level = 0.95
var_95 = np.percentile(portfolio_returns, (1 - confidence_level) * 100)

investment = 10000000 
potential_loss = investment * var_95

print(f"--- RISK REPORT (VaR) ---")
print(f"Confidence Level: {confidence_level*100}% ")
print(f"Daily VaR %:      {var_95*100:.2f}%")
print(f"Potential 1-Day Loss: ₹{abs(potential_loss):,.2f}")

plt.hist(portfolio_returns, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(var_95, color='red', linestyle='dashed', linewidth=2, label=f'VaR 95% ({var_95*100:.2f}%)')
plt.title('Portfolio Returns Distribution & VaR Risk Threshold')
plt.legend()
plt.show()