import numpy as np
import matplotlib.pyplot as plt


def simulate_hawkes(mu, alpha, beta, T):
    t = 0
    points = []
    curr_intensity = mu
    
    while t < T:
        upper_bound = mu + np.sum(alpha * np.exp(-beta * (t - np.array(points))))
        
        dt = -np.log(np.random.uniform()) / upper_bound
        t += dt
        
        actual_intensity = mu + np.sum(alpha * np.exp(-beta * (t - np.array(points))))
        
        if np.random.uniform() < actual_intensity / upper_bound:
            points.append(t)
            
    return np.array(points)

mu = 0.5   
alpha = 0.8 
beta = 1.2  
T = 100     

arrival_times = simulate_hawkes(mu, alpha, beta, T)

time_grid = np.linspace(0, T, 1000)
intensity = []
for t in time_grid:
    past_points = arrival_times[arrival_times < t]
    lambda_t = mu + np.sum(alpha * np.exp(-beta * (t - past_points)))
    intensity.append(lambda_t)

plt.figure(figsize=(12, 5))
plt.plot(time_grid, intensity, color='darkred', linewidth=1.5, label='Trading Intensity')
plt.scatter(arrival_times, [0]*len(arrival_times), color='black', s=10, marker='|', label='Trade Executed')
plt.title(f'Hawkes Process: Modeling Order Clustering (Alpha={alpha})')
plt.ylabel('Market Activity Level')
plt.xlabel('Time (Seconds)')
plt.legend()
plt.show()

print(f"Total Trades: {len(arrival_times)}")
print("Tier 1 Insight: Notice the spikes?")
print("One trade triggers a chain reaction. Standard models assume trades are independent. They are wrong.")