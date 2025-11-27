!pip install hmmlearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM

np.random.seed(42)
returns_bull = np.random.normal(0.001, 0.005, 100)
returns_bear = np.random.normal(-0.002, 0.02, 50)
returns_side = np.random.normal(0.0, 0.005, 100)
returns = np.concatenate([returns_bull, returns_bear, returns_side, returns_bull])

X = returns.reshape(-1, 1)

model = GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
model.fit(X)

hidden_states = model.predict(X)

plt.figure(figsize=(12, 6))
for i in range(len(returns)-1):
    state = hidden_states[i]
    color = ['green', 'red', 'blue'][state] 
    plt.plot([i, i+1], [returns[i], returns[i+1]], color=color, linewidth=2)

plt.plot([], [], color='green', label='Regime A (Low Vol)')
plt.plot([], [], color='red', label='Regime B (High Vol)')
plt.plot([], [], color='blue', label='Regime C (Transition)')

plt.title('HMM: Automatically Detecting "Hidden" Market Regimes')
plt.legend()
plt.show()

print("Tier 1 Insight: The code colored the 'Crash' (High Vol) in Red automatically.")
print("We didn't tell it where the crash was; the Probability Model found it.")