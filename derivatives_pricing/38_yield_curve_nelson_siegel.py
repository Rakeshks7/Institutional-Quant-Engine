import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def nelson_siegel(t, b0, b1, b2, tau):
    term1 = (1 - np.exp(-t/tau)) / (t/tau)
    term2 = term1 - np.exp(-t/tau)
    return b0 + b1 * term1 + b2 * term2

maturities = np.array([1, 2, 3, 5, 7, 10, 30])
market_yields = np.array([5.0, 5.2, 5.4, 5.8, 6.1, 6.5, 6.8]) 

def objective_function(params):
    b0, b1, b2, tau = params
    model_yields = nelson_siegel(maturities, b0, b1, b2, tau)
    return np.sum((market_yields - model_yields) ** 2)

initial_guess = [5, -2, 2, 2] 
result = minimize(objective_function, initial_guess, bounds=((0, 15), (-10, 10), (-10, 10), (0.1, 10)))
fitted_params = result.x

t_smooth = np.linspace(0.5, 30, 100)
fitted_yields = nelson_siegel(t_smooth, *fitted_params)

plt.figure(figsize=(10, 6))
plt.scatter(maturities, market_yields, color='red', label='Observed Market Bonds', s=50)
plt.plot(t_smooth, fitted_yields, color='blue', label='Fitted Nelson-Siegel Curve')
plt.title('Fixed Income: Yield Curve Construction')
plt.xlabel('Maturity (Years)')
plt.ylabel('Yield (%)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

print(f"--- FITTED PARAMETERS ---")
print(f"Long Term Level (B0): {fitted_params[0]:.2f}%")
print(f"Short Term Slope (B1): {fitted_params[1]:.2f}")
print(f"Hump/Curvature (B2):   {fitted_params[2]:.2f}")
print("Insight: If a real bond dot is ABOVE the blue line, it yields too much. BUY IT.")