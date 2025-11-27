import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

strikes = np.linspace(2000, 3000, 20)  
maturities = np.linspace(10, 90, 10)   

X, Y = np.meshgrid(strikes, maturities)

Z = 0.2 + (0.000001 * (X - 2500)**2) + (0.01 / (Y/365))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('Strike Price')
ax.set_ylabel('Days to Maturity')
ax.set_zlabel('Implied Volatility (IV)')
ax.set_title('3D Volatility Surface (The "Smile" & Term Structure)')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()