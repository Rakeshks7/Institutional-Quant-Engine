import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 100      
Barrier = 120 
T = 1.0
r = 0.05
sigma = 0.2
simulations = 10000
steps = 252 

dt = T/steps
nudt = (r - 0.5 * sigma**2) * dt
volsdt = sigma * np.sqrt(dt)

random_shocks = np.random.normal(0, 1, (steps, simulations))
paths = S0 * np.exp(np.cumsum(nudt + volsdt * random_shocks, axis=0))

max_prices = np.max(paths, axis=0)

payoffs = np.where(max_prices >= Barrier, 0, np.maximum(paths[-1] - K, 0))

option_price = np.exp(-r * T) * np.mean(payoffs)

plt.figure(figsize=(10, 6))
plt.plot(paths[:, :50], alpha=0.4, color='gray')
plt.axhline(Barrier, color='red', linestyle='--', linewidth=2, label='Knock-Out Barrier (120)')
plt.title(f'Barrier Option Simulation: {option_price:.2f} Premium')
plt.legend()
plt.show()

print(f"--- EXOTIC PRICING ---")
print(f"Vanilla Call Price (Approx): ₹{S0*0.08:.2f}") 
print(f"Barrier Call Price:          ₹{option_price:.2f}")
print("Insight: The Barrier option is cheaper because there is a risk it dies.")