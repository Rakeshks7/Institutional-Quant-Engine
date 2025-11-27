import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

tickers = ['HDFCBANK.NS', 'ICICIBANK.NS', 'TCS.NS', 'INFY.NS', 'SUNPHARMA.NS', 'CIPLA.NS']
np.random.seed(42)
data = pd.DataFrame(np.random.randn(100, 6), columns=tickers)
data['ICICIBANK.NS'] += data['HDFCBANK.NS'] * 0.8
data['INFY.NS'] += data['TCS.NS'] * 0.8

corr = data.corr()

dist = np.sqrt((1 - corr) / 2)
link = linkage(dist, 'single')

plt.figure(figsize=(10, 6))
dendrogram(link, labels=tickers, leaf_rotation=90)
plt.title('Hierarchical Clustering (HRP): Finding Asset Clusters')
plt.ylabel('Distance (Dissimilarity)')
plt.show()

print("--- HRP INSIGHT ---")
print("Notice how HDFC and ICICI are linked first? The algorithm treats them as one 'Risk Cluster'.")
print("A 'No. 1 Player' allocates capital to the CLUSTERS, not individual stocks.")