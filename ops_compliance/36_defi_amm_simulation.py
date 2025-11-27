import numpy as np
import matplotlib.pyplot as plt

class UniswapPool:
    def __init__(self, eth_res, usdc_res):
        self.x = eth_res    
        self.y = usdc_res   
        self.k = self.x * self.y 
        
    def get_price(self):
        return self.y / self.x 
    
    def swap_eth_for_usdc(self, eth_in):
        x_new = self.x + eth_in
        y_new = self.k / x_new
        dy = self.y - y_new 
        
        self.x = x_new
        self.y = y_new
        return dy


pool = UniswapPool(eth_res=100, usdc_res=200000) 
binance_price = 1950 

print(f"Initial Pool Price: ${pool.get_price():.2f}")
print(f"Binance Price:      ${binance_price:.2f}")


target_x = np.sqrt(pool.k / binance_price)
eth_to_dump = target_x - pool.x

print(f"--- ARBITRAGE EXECUTION ---")
print(f"Bot detects opportunity. Dumps {eth_to_dump:.4f} ETH into Pool.")

usdc_received = pool.swap_eth_for_usdc(eth_to_dump)
print(f"New Pool Price:     ${pool.get_price():.2f} (Equilibrium Restored)")
print(f"Bot received:       ${usdc_received:.2f} USDC")

cost = eth_to_dump * binance_price
profit = usdc_received - cost

print(f"Bot Profit:         ${profit:.2f} (Risk Free)")