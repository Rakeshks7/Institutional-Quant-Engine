import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_measurement_variance):
        self.Q = process_variance
        self.R = measurement_variance
        self.P = estimated_measurement_variance
        self.X = 0 

    def update(self, measurement):
        self.P = self.P + self.Q
        
        K = self.P / (self.P + self.R)
        self.X = self.X + K * (measurement - self.X)
        self.P = (1 - K) * self.P
        return self.X

data = yf.download("INFY.NS", start="2023-01-01", end="2024-01-01")['Close']

kf = KalmanFilter(process_variance=1e-5, measurement_variance=0.01, estimated_measurement_variance=1.0)

kalman_estimates = []
for price in data.values:
    kalman_estimates.append(kf.update(price))

data_kf = pd.Series(kalman_estimates, index=data.index)

subset = data.iloc[-100:]
subset_kf = data_kf.iloc[-100:]
subset_sma = data.rolling(window=20).mean().iloc[-100:] 

plt.figure(figsize=(12, 6))
plt.plot(subset, label='Actual Price (Noisy)', color='gray', alpha=0.5)
plt.plot(subset_sma, label='SMA 20 (Lagging)', color='green', linestyle='--')
plt.plot(subset_kf, label='Kalman Filter (Responsive)', color='blue', linewidth=2)
plt.title('Kalman Filter vs. Moving Average')
plt.legend()
plt.show()