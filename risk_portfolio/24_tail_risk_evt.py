import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import genpareto

np.random.seed(42)
normal_returns = np.random.normal(0, 0.01, 1000)
crash_events = np.random.uniform(-0.10, -0.05, 10) 
returns = np.concatenate([normal_returns, crash_events])

threshold = np.percentile(returns, 5) 
tail_losses = sorted(returns[returns < threshold]) 
tail_losses = np.abs(tail_losses) 

shape, loc, scale = genpareto.fit(tail_losses)

var_99 = threshold
evt_cvar = np.mean(tail_losses) 

print(f"--- BLACK SWAN DEFENSE (EVT) ---")
print(f"Normal VaR Threshold: {threshold:.4f}")
print(f"GPD Shape Parameter:  {shape:.4f} (Positive = Fat Tails/Dangerous)")
print(f"EVT-Adjusted CVaR:    {evt_cvar:.4f} (Expected loss during crash)")

plt.hist(returns, bins=50, alpha=0.6, label='Normal Returns')
plt.hist(crash_events, bins=10, color='red', alpha=1.0, label='Black Swans')
plt.title('Extreme Value Theory: Modeling the Unthinkable')
plt.legend()
plt.show()