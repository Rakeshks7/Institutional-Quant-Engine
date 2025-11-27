import numpy as np
import pandas as pd

market_caps = np.array([500000, 400000, 800000])
market_weights = market_caps / np.sum(market_caps) # [0.29, 0.23, 0.47]

sigma = np.array([
    [0.04, 0.02, 0.02],
    [0.02, 0.05, 0.03],
    [0.02, 0.03, 0.06]
])
risk_aversion_delta = 2.5 

tau = 0.05 
implied_returns = risk_aversion_delta * np.dot(sigma, market_weights)

P = np.array([[0, 1, -1]]) 
Q = np.array([0.02])
omega = np.dot(np.dot(P, sigma), P.T) * tau 


inv_tau_sigma = np.linalg.inv(tau * sigma)
inv_omega = np.linalg.inv(omega)

term1 = np.linalg.inv(inv_tau_sigma + np.dot(np.dot(P.T, inv_omega), P))
term2 = np.dot(inv_tau_sigma, implied_returns) + np.dot(np.dot(P.T, inv_omega), Q)

bl_returns = np.dot(term1, term2)

print("--- BLACK-LITTERMAN RESULTS ---")
print(f"Asset Names:      ['HDFC', 'TCS', 'RELIANCE']")
print(f"Market Consensus: {implied_returns.round(4)}")
print(f"Your View:        'TCS will beat Reliance by 2%'")
print(f"BL New Forecast:  {bl_returns.round(4)}")
print("Insight: Notice TCS Expected Return went UP, and Reliance went DOWN.")
print("The model blended the market reality with your opinion mathematically.")