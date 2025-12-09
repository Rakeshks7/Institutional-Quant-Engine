import ray
import time
import numpy as np

if ray.is_initialized(): ray.shutdown()
ray.init(ignore_reinit_error=True)

def _heavy_computation_impl(stock_id):
    time.sleep(1) 
    return f"Stock {stock_id}: Analyzed"

@ray.remote
def heavy_computation(stock_id):
    return _heavy_computation_impl(stock_id)

stocks = range(10) 

print(f"--- DISTRIBUTED COMPUTING TEST ---")

start = time.time()
results_seq = [_heavy_computation_impl(s) for s in stocks] 
end = time.time()
print(f"🐢 Sequential Python: {end - start:.2f} seconds")

start = time.time()
futures = [heavy_computation.remote(s) for s in stocks]
results_par = ray.get(futures)
end = time.time()
print(f"🚀 Ray Distributed:   {end - start:.2f} seconds")

print("Insight: Ray creates a 'Serverless' experience. 5 hours becomes 5 minutes.")
ray.shutdown()
