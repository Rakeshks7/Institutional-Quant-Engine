import numpy as np
import matplotlib.pyplot as plt

days = 90 
avg_temp = 30 
volatility = 5

np.random.seed(42)
temps = np.random.normal(avg_temp, volatility, days)

HDD = np.maximum(65 - temps, 0)
cumulative_hdd = np.cumsum(HDD)

strike_hdd = 3000
tick_value = 100 

final_hdd = cumulative_hdd[-1]
payoff = max(0, final_hdd - strike_hdd) * tick_value

plt.figure(figsize=(10, 6))
plt.plot(cumulative_hdd, label='Accumulated HDD (Coldness)', color='blue')
plt.axhline(strike_hdd, color='red', linestyle='--', label=f'Strike ({strike_hdd})')
plt.title(f'Weather Derivative: Winter HDD Call Option')
plt.ylabel('Heating Degree Days')
plt.xlabel('Days into Winter')
plt.legend()
plt.show()

print(f"--- WEATHER DESK ---")
print(f"Season Total HDD: {final_hdd:.2f}")
print(f"Strike HDD:       {strike_hdd}")
print(f"Option Payoff:    ${payoff:.2f}")
print("Insight: A Gas company buys this. If winter is warm (Low HDD), they lose gas sales but get paid by this option.")