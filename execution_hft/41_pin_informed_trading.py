import numpy as np
from scipy.optimize import minimize

buys = np.array([100, 110, 150, 400, 450, 420, 120]) 
sells = np.array([100, 105, 95, 100, 90, 85, 100])   

def pin_likelihood(params, B, S):
    alpha, delta, mu, epsilon = params

    imbalance = np.abs(B - S)
    expected_imbalance = alpha * mu
    
    return np.sum((imbalance - expected_imbalance)**2)

initial_guess = [0.2, 0.5, 300, 100] 
result = minimize(pin_likelihood, initial_guess, args=(buys, sells), bounds=((0,1), (0,1), (0, 1000), (0, 1000)))

alpha_est, delta_est, mu_est, eps_est = result.x

PIN = (alpha_est * mu_est) / (alpha_est * mu_est + 2 * eps_est)

print("--- MICROSTRUCTURE INSIGHT ---")
print(f"Est. Informed Order Rate (Mu): {mu_est:.0f} orders")
print(f"Est. Noise Order Rate (Eps):   {eps_est:.0f} orders")
print(f"PIN (Prob of Informed Trading): {PIN:.4f}")

if PIN > 0.3:
    print("⚠️ WARNING: High likelihood of Insider/Informed Activity.")