import pandas as pd
import numpy as np

class Exchange:
    def __init__(self, name, bid_price, liquidity, fee):
        self.name = name
        self.bid = bid_price
        self.liquidity = liquidity
        self.fee = fee 

nse = Exchange("NSE", bid_price=100.05, liquidity=500, fee=0.003)
bse = Exchange("BSE", bid_price=100.00, liquidity=1000, fee=0.003)
dark_pool = Exchange("DARK", bid_price=100.02, liquidity=2000, fee=0.001)

exchanges = [nse, bse, dark_pool]


def smart_route(order_qty, venues):
    print(f"--- SOR: Routing Sell Order for {order_qty} shares ---")
    
    for ex in venues:
        ex.effective_px = ex.bid - ex.fee
        
    sorted_venues = sorted(venues, key=lambda x: x.effective_px, reverse=True)
    
    remaining_qty = order_qty
    fills = []
    
    for ex in sorted_venues:
        if remaining_qty <= 0: break
        
        fill_qty = min(remaining_qty, ex.liquidity)
        fills.append({
            'Venue': ex.name,
            'Price': ex.bid,
            'Fee': ex.fee,
            'Qty': fill_qty,
            'Net_Proceeds': fill_qty * (ex.bid - ex.fee)
        })
        
        remaining_qty -= fill_qty
        
    return fills, remaining_qty

fills, left = smart_route(2000, exchanges)

total_proceeds = sum(f['Net_Proceeds'] for f in fills)
avg_price = total_proceeds / 2000

print(f"{'VENUE':<10} | {'QTY':<5} | {'PRICE':<8} | {'NET PROCEEDS'}")
print("-" * 50)
for f in fills:
    print(f"{f['Venue']:<10} | {f['Qty']:<5} | {f['Price']:<8} | {f['Net_Proceeds']:.2f}")

print("-" * 50)
print(f"Average Fill Price: {avg_price:.4f}")
print("Insight: The SOR didn't just dump on BSE (lowest price).")
print("It skimmed the top of NSE and Dark Pool first to maximize profit.")