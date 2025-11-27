import numpy as np
import matplotlib.pyplot as plt

class MarketMaker:
    def __init__(self, s0, inventory=0):
        self.s = s0         
        self.q = inventory  
        self.sigma = 2      
        self.gamma = 0.1    
        self.k = 1.5        

    def calculate_quotes(self):
        r = self.s - (self.q * self.gamma * (self.sigma**2))
        
        spread = (self.gamma * (self.sigma**2)) + (2 / self.gamma) * np.log(1 + (self.gamma / self.k))
        
        bid_price = r - (spread / 2)
        ask_price = r + (spread / 2)
        
        return r, bid_price, ask_price

mm = MarketMaker(s0=100)
inventory_levels = range(-10, 11) 
bids, asks, reserves = [], [], []

for q in inventory_levels:
    mm.q = q
    r, b, a = mm.calculate_quotes()
    bids.append(b)
    asks.append(a)
    reserves.append(r)

plt.figure(figsize=(10, 6))
plt.plot(inventory_levels, bids, label='My Bid Price', color='green', marker='o')
plt.plot(inventory_levels, asks, label='My Ask Price', color='red', marker='o')
plt.plot(inventory_levels, reserves, label='Reservation Price (Indifference)', color='black', linestyle='--')
plt.axvline(0, color='gray', alpha=0.3)
plt.xlabel('My Inventory Position (q)')
plt.ylabel('Price')
plt.title('Avellaneda-Stoikov: Dynamic Pricing based on Inventory Risk')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("Insight: Notice when Inventory is +10 (Long), both Bid and Ask DROP.")
print("The algo is desperate to SELL and reluctant to BUY.")