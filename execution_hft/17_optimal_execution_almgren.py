import numpy as np
import matplotlib.pyplot as plt

def optimal_trajectory(total_shares, days, risk_aversion):
    
    time = np.linspace(0, days, 20)
    
    kappa = risk_aversion * 0.5 
    shares_remaining = total_shares * (np.sinh(kappa * (days - time)) / np.sinh(kappa * days))
    
    return time, shares_remaining

total_shares = 100000
days = 1

t1, strategy_aggressive = optimal_trajectory(total_shares, days, risk_aversion=10.0)
t2, strategy_passive = optimal_trajectory(total_shares, days, risk_aversion=0.1)

plt.figure(figsize=(10, 6))
plt.plot(t1, strategy_aggressive, label='Aggressive (High Urgency)', color='red', linestyle='--')
plt.plot(t2, strategy_passive, label='Passive (Minimize Impact)', color='green')
plt.plot([0, 1], [100000, 0], label='TWAP (Linear Benchmark)', color='gray', alpha=0.5)

plt.title('Optimal Execution Trajectory (Almgren-Chriss Model)')
plt.xlabel('Time (Days)')
plt.ylabel('Shares Remaining')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()