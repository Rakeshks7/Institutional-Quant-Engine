import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.linspace(0, 100, 100)
true_beta = np.linspace(1.5, 2.0, 100) 
asset_a = np.random.normal(0, 1, 100)
asset_b = (true_beta * asset_a) + np.random.normal(0, 0.5, 100) 

delta = 0.0001 
V_w = delta / (1 - delta) * np.eye(2)
V_v = 1.0 

theta = np.zeros(2) 
P = np.eye(2) 

beta_estimates = []

for i in range(len(x)):
    F = np.array([asset_a[i], 1.0]).reshape(1, 2)
    
    y = asset_b[i]
    
    R = P + V_w 
    
    y_hat = F @ theta 
    e = y - y_hat     
    Q = F @ R @ F.T + V_v 
    
    K = R @ F.T @ np.linalg.inv(Q)
    
    theta = theta + K.flatten() * e
    P = (np.eye(2) - K @ F) @ R
    
    beta_estimates.append(theta[0])

plt.figure(figsize=(10, 6))
plt.plot(true_beta, label='True Hidden Ratio (1.5 -> 2.0)', color='black', linestyle='--')
plt.plot(beta_estimates, label='Kalman Estimated Ratio', color='blue')
plt.title('Dynamic Hedging: Tracking a Changing Relationship')
plt.legend()
plt.show()

print("Tier 1 Insight: Standard regression fails here.")
print("The Kalman Filter 'learns' that the hedge ratio is shifting from 1.5 to 2.0.")