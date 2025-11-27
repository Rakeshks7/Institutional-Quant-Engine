import numpy as np
import matplotlib.pyplot as plt

mu = 0.15   
r = 0.05    
sigma = 0.20 

optimal_f = (mu - r) / (sigma**2)


days = 252 * 5 
dt = 1/252
drift = (mu - 0.5 * sigma**2) * dt
vol_shock = sigma * np.sqrt(dt)

equity_half = [100]
equity_full = [100]
equity_double = [100]

np.random.seed(42)
shocks = np.random.normal(0, 1, days)

for t in range(days):
    ret = drift + vol_shock * shocks[t]
    
    equity_half.append(equity_half[-1] * (1 + (optimal_f * 0.5) * ret))
    equity_full.append(equity_full[-1] * (1 + optimal_f * ret))
    equity_double.append(equity_double[-1] * (1 + (optimal_f * 2.0) * ret))

plt.figure(figsize=(10, 6))
plt.plot(equity_half, label='Half Kelly (Safe)', color='green')
plt.plot(equity_full, label='Full Kelly (Optimal Growth)', color='blue')
plt.plot(equity_double, label='Double Kelly (Too Risky)', color='red', linestyle='--')
plt.title(f'The Knife Edge of Position Sizing (Optimal Leverage: {optimal_f:.2f}x)')
plt.ylabel('Wealth')
plt.yscale('log') 
plt.legend()
plt.show()

print("Tier 1 Insight: Look at the Red Line (Double Kelly).")
print("Even though they bet MORE on a winning stock, they ended up with LESS money.")
print("Volatility Drag kills over-leveraged traders.")