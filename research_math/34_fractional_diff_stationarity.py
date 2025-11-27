import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_weights(d, size):
    w = [1.0]
    for k in range(1, size):
        w_new = -w[-1] / k * (d - k + 1)
        w.append(w_new)
    return np.array(w[::-1]).reshape(-1, 1) 

def frac_diff(series, d, threshold=1e-5):
    weights = get_weights(d, len(series))
    weights = np.array(weights).flatten()
    
    if np.sum(np.abs(weights)) < threshold: return None
    
    df_fd = pd.Series(index=series.index, dtype='float64')
    
    for i in range(len(weights), len(series)):
        val = np.dot(weights, series.iloc[i-len(weights):i])
        df_fd.iloc[i] = val
        
    return df_fd.dropna()

np.random.seed(42)
price = np.cumsum(np.random.normal(0.1, 1, 1000)) + 100
price_series = pd.Series(price)

fd_series = frac_diff(price_series, d=0.4)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

ax1.plot(price_series, color='black')
ax1.set_title('Original Price (Non-Stationary - ML Fails)')

ax2.plot(price_series.diff(), color='gray', alpha=0.6)
ax2.set_title('Standard Difference d=1.0 (Memory Erased - No Trend)')

ax3.plot(fd_series, color='blue')
ax3.set_title('Fractional Difference d=0.4 (Stationary BUT keeps Trend Memory)')

plt.tight_layout()
plt.show()

print("Tier 1 Insight: Look at the Blue line.")
print("It is flat (stationary) like the Gray line, but it preserves the 'bumps' of the original trend.")
print("This allows Neural Networks to learn long-term patterns.")