import numpy as np
import matplotlib.pyplot as plt

S0 = 100.0     
v0 = 0.04      
rho = -0.7     
kappa = 2.0    
theta = 0.04   
sigma_v = 0.3  
T = 1.0        
dt = 1/252     

np.random.seed(42)
N = int(T/dt)
num_sims = 5  

means = [0, 0]
covs = [[1, rho], [rho, 1]]
Z = np.random.multivariate_normal(means, covs, (num_sims, N))
Z_s = Z[:,:,0] 
Z_v = Z[:,:,1] 

prices = np.zeros((num_sims, N))
variances = np.zeros((num_sims, N))

prices[:, 0] = S0
variances[:, 0] = v0

for t in range(1, N):
    v_prev = variances[:, t-1]
    s_prev = prices[:, t-1]
    
    v_prev = np.maximum(v_prev, 0)
    
    dv = kappa * (theta - v_prev) * dt + sigma_v * np.sqrt(v_prev * dt) * Z_v[:, t]
    variances[:, t] = v_prev + dv
    
    ds = s_prev * np.sqrt(v_prev * dt) * Z_s[:, t]
    prices[:, t] = s_prev + ds

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

for i in range(num_sims):
    ax1.plot(prices[i], linewidth=1)
    ax2.plot(np.sqrt(np.maximum(variances[i], 0)), linewidth=1) 

ax1.set_title('Heston Model: Stock Price Paths')
ax1.set_ylabel('Price')
ax2.set_title('Stochastic Volatility Paths (Note: It changes over time!)')
ax2.set_ylabel('Volatility')
plt.xlabel('Time Steps')
plt.show()

print("Tier 1 Insight: Notice how Volatility spikes when Prices drop?")
print("This 'Leverage Effect' (Rho = -0.7) is what makes Heston superior to Black-Scholes.")