import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t

rho = 0.8 
df = 2    

mean = [0, 0]
cov = [[1, rho], [rho, 1]]
x = np.random.multivariate_normal(mean, cov, 1000)

u = t.cdf(x, df)

asset_1 = norm.ppf(u[:, 0])
asset_2 = norm.ppf(u[:, 1])

plt.figure(figsize=(8, 8))
plt.scatter(asset_1, asset_2, alpha=0.5, s=10)
plt.title('T-Copula Simulation: Tail Dependence')
plt.xlabel('Asset A Returns')
plt.ylabel('Asset B Returns')

plt.axvline(-2, color='red', linestyle='--')
plt.axhline(-2, color='red', linestyle='--')
plt.text(-3, -3, "CRASH ZONE\n(Highly Linked)", color='red', fontweight='bold')

plt.grid(True, alpha=0.3)
plt.show()

print("Insight: Notice how points cluster in the bottom-left corner?")
print("Standard correlation ignores this. Copulas capture this 'Panic Link'.")