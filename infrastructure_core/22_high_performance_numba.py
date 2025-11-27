import numpy as np
import time
from numba import jit

def python_moving_average(data, window):
    result = np.zeros(len(data))
    for i in range(len(data)):
        if i >= window:
            result[i] = np.mean(data[i-window:i])
    return result

@jit(nopython=True)
def fast_moving_average(data, window):
    result = np.zeros(len(data))
    for i in range(window, len(data)):
        total = 0.0
        for j in range(window):
            total += data[i-j-1]
        result[i] = total / window
    return result

data = np.random.random(10_000_000) 
window = 50

print("🏎️ STARTING SPEED TEST (10 Million rows)...")

start = time.time()
python_moving_average(data, window)
py_time = time.time() - start
print(f"🐢 Pure Python: {py_time:.4f} seconds")

start = time.time()
fast_moving_average(data, window)
numba_time = time.time() - start
print(f"🚀 Numba JIT:  {numba_time:.4f} seconds")

speedup = py_time / numba_time
print(f"⚡ SPEEDUP FACTOR: {speedup:.0f}x Faster")
print("(This is why High Frequency Traders use JIT optimization)")