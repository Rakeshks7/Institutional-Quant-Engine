import time
import random

class IcebergAlgo:
    def __init__(self, initial_capital=10000000): 
        self.capital = initial_capital

    def get_market_price(self, symbol):
        base_price = 2500.00
        noise = random.uniform(-2, 2) 
        return round(base_price + noise, 2)

    def execute_iceberg(self, symbol, total_qty, slice_qty, time_delay=2):
        print(f"🧊 INITIATING ICEBERG ORDER: Buy {total_qty} {symbol}")
        print(f"   Hidden Quantity: {total_qty}")
        print(f"   Visible Slice:   {slice_qty}")
        print("-" * 50)
        
        remaining_qty = total_qty
        total_cost = 0
        order_count = 1

        while remaining_qty > 0:
            current_slice = min(slice_qty, remaining_qty)
            
            price = self.get_market_price(symbol)
            
            cost = current_slice * price
            self.capital -= cost
            total_cost += cost
            remaining_qty -= current_slice
            
            print(f"✅ Child Order #{order_count}: BOUGHT {current_slice} @ ₹{price}")
            print(f"   🌊 Remaining Hidden: {remaining_qty}")
            
            order_count += 1
            
            if remaining_qty > 0:
                print(f"   ⏳ Waiting {time_delay}s for liquidity...")
                time.sleep(time_delay)
        
        avg_price = total_cost / total_qty
        print("-" * 50)
        print(f"🎉 EXECUTION COMPLETE")
        print(f"   Total Bought: {total_qty} {symbol}")
        print(f"   Avg Price:    ₹{avg_price:.2f}")
        print(f"   Total Cost:   ₹{total_cost:.2f}")

algo = IcebergAlgo()

algo.execute_iceberg(symbol="RELIANCE", total_qty=5000, slice_qty=1000, time_delay=1)