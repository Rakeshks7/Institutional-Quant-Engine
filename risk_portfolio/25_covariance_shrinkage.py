import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.covariance import LedoitWolf

np.random.seed(42)
dummy_returns = np.random.normal(0, 0.01, (100, 50)) 

sample_cov = np.cov(dummy_returns, rowvar=False)

lw = LedoitWolf()
shrunk_cov = lw.fit(dummy_returns).covariance_

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.heatmap(sample_cov[:15, :15], ax=ax1, cmap='coolwarm', center=0)
ax1.set_title('Standard Covariance (Noisy/Extreme)')

sns.heatmap(shrunk_cov[:15, :15], ax=ax2, cmap='coolwarm', center=0)
ax2.set_title('Ledoit-Wolf Shrinkage (Stable/Robust)')

plt.show()

print("--- STABILITY REPORT ---")
print("Notice the 'Standard' matrix has extreme red/blue spots (False correlations).")
print("The 'Shrunk' matrix dampens these extremes.")
print("Tier 1 Insight: Never feed a raw covariance matrix into an optimizer.")