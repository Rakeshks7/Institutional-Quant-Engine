import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

np.random.seed(42)
days = 252
market = np.random.normal(0, 0.01, days)
rates = np.random.normal(0, 0.01, days)

s1 = 1.0*market + 0.1*np.random.normal(0, 0.005, days) 
s2 = 0.9*market + 0.0*np.random.normal(0, 0.005, days) 
s3 = 0.5*market + 0.8*rates 
s4 = 0.4*market + 0.9*rates 

data = pd.DataFrame({'Tech': s1, 'Consumer': s2, 'Bank': s3, 'RealEstate': s4})

pca = PCA(n_components=4)
pca.fit(data)

variance = pca.explained_variance_ratio_

plt.figure(figsize=(8, 5))
plt.bar(['Factor 1', 'Factor 2', 'Factor 3', 'Factor 4'], variance*100, color='purple')
plt.title('PCA: Decomposing Risk Drivers')
plt.ylabel('Variance Explained (%)')
plt.show()

print("--- RISK ANALYSIS ---")
print(f"Factor 1 (The Market) explains: {variance[0]*100:.1f}% of all movement.")
print(f"Factor 2 (Rates) explains:      {variance[1]*100:.1f}% of all movement.")
print("Insight: Even though you own 4 stocks, ~95% of your risk comes from just 2 Factors.")
print("Diversification is an illusion if you don't check PCA.")