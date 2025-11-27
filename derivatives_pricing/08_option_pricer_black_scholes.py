import numpy as np
from scipy.stats import norm

# INPUTS
S = 2400   
K = 2450   
T = 30/365 
r = 0.07   
sigma = 0.20 

def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1
        
    return price, delta

call_price, call_delta = black_scholes(S, K, T, r, sigma, "call")
put_price, put_delta = black_scholes(S, K, T, r, sigma, "put")

print(f"--- BLACK SCHOLES PRICING ---")
print(f"Spot: {S}, Strike: {K}, Vol: {sigma*100}%")
print(f"CALL Price: ₹{call_price:.2f} | Delta: {call_delta:.2f}")
print(f"PUT Price:  ₹{put_price:.2f}  | Delta: {put_delta:.2f}")