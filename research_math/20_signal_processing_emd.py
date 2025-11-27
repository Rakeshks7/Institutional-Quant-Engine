import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

t = np.linspace(0, 1, 200)
trend = 100 + 50*t 
cycle = 10 * np.sin(2*np.pi*10*t) 
noise = 5 * np.random.normal(size=len(t)) 

price = trend + cycle + noise

imf_noise = noise
imf_cycle = cycle
residue_trend = trend

analytic_signal = hilbert(imf_cycle)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) / (2.0*np.pi) * 200)

fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

axes[0].plot(t, price, 'k')
axes[0].set_title('Raw Market Data (Noisy)')

axes[1].plot(t, imf_noise, 'gray', alpha=0.6)
axes[1].set_title('IMF 1: High Freq Noise (Algo Trading)')

axes[2].plot(t, imf_cycle, 'b')
axes[2].set_title('IMF 2: Market Cycles (Swing Trading)')

axes[3].plot(t, residue_trend, 'r', linewidth=2)
axes[3].set_title('Residue: The True Trend (Long Term)')

plt.tight_layout()
plt.show()

print("Tier 1 Insight: We don't trade the Raw Data.")
print("We trade IMF 2 (Cycles) and ignore IMF 1 (Noise).")