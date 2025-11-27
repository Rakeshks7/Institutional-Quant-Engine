import numpy as np
import matplotlib.pyplot as plt

class AtomicClock:
    def __init__(self, name, drift_per_sec):
        self.name = name
        self.true_time = 0.0
        self.drift_rate = drift_per_sec 
        
    def tick(self, dt):
        self.true_time += dt
        return self.true_time + (self.true_time * self.drift_rate) + np.random.normal(0, 1e-6)

exchange_clock = AtomicClock("NSE_Master", 0.0)
my_server_clock = AtomicClock("Algo_Server", 1e-4) 

times = []
offsets = []

estimated_offset = 0

print("--- CLOCK SYNCHRONIZATION (PTP) ---")
for t in range(100):
    dt = 1.0
    t1_exchange = exchange_clock.tick(dt)
    t2_server = my_server_clock.tick(dt)
    
    raw_diff = t2_server - t1_exchange
    
    estimated_offset = (0.9 * estimated_offset) + (0.1 * raw_diff)
    
    corrected_time = t2_server - estimated_offset
    error = corrected_time - t1_exchange
    
    times.append(t)
    offsets.append(error * 1e6) 

    if t % 20 == 0:
        print(f"Tick {t}: Raw Drift: {raw_diff*1e6:.2f}µs | Corrected Error: {error*1e6:.2f}µs")

plt.figure(figsize=(10, 5))
plt.plot(times, offsets, color='green')
plt.axhline(0, color='black', linestyle='--')
plt.title('PTP Clock Correction: Keeping Error near Zero')
plt.ylabel('Error (Microseconds)')
plt.xlabel('Time (Seconds)')
plt.show()

print("Tier 1 Insight: Without PTP, the drift (Raw Diff) keeps growing.")
print("With PTP, we stay locked to the Exchange Time within microseconds.")