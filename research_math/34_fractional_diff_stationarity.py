import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_weights(d, size, threshold=1e-5):
    w = [1.0]
    for k in range(1, size):
        w_new = -w[-1] / k * (d - k + 1)
        if abs(w_new) < threshold: 
            break
        w.append(w_new)
        
    return np.array(w[::-1])

def frac_diff(series, d, threshold=1e-5):
    weights = get_weights(d, len(series), threshold)
    width = len(weights)
    
    df_fd = pd.Series(index=series.index, dtype='float64')
    
    if width >= len(series):
        raise ValueError("Data too short for this threshold/d combo!")
        
    weights_arr = np.array(weights).flatten()
    
    for i in range(width, len(series)):
        window = series.iloc[i-width:i].values
        val = np.dot(weights_arr, window)
        df_fd.iloc[i] = val
        
    return df_fd.dropna()

np.random.seed(42)
price = np.cumsum(np.random.normal(0.1, 1, 1000)) + 100
price_series = pd.Series(price)

fd_series = frac_diff(price_series, d=0.4, threshold=1e-4)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

ax1.plot(price_series, color='black')
ax1.set_title('Original Price (Non-Stationary - ML Fails)')
ax1.grid(True, alpha=0.3)

ax2.plot(price_series.diff(), color='gray', alpha=0.6)
ax2.set_title('Standard Difference d=1.0 (Memory Erased - No Trend)')
ax2.grid(True, alpha=0.3)

ax3.plot(fd_series, color='blue', linewidth=1)
ax3.set_title('Fractional Difference d=0.4 (Stationary BUT keeps Trend Memory)')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("--- DIAGNOSTIC ---")
print(f"Original Length: {len(price_series)}")
print(f"FracDiff Length: {len(fd_series)} (Should be > 0)")
print("If the bottom plot is a blue line oscillating around 0 but looking 'trendier' than the gray one, it worked.")
