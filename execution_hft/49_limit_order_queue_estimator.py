import collections

class QueueTracker:
    def __init__(self, my_order_id, my_qty):
        self.my_order_id = my_order_id
        self.my_qty = my_qty
        self.orders_ahead = 10000 
        self.my_position = self.orders_ahead
        self.is_filled = False

    def process_trade(self, trade_qty):
        if self.is_filled: return
        
        print(f"⚡ TRADE PRINTED: {trade_qty} shares bought.")
        
        if self.orders_ahead > 0:
            if trade_qty < self.orders_ahead:
                self.orders_ahead -= trade_qty
                print(f"   Queue decreases. {self.orders_ahead} shares still ahead of me.")
            else:
                remainder = trade_qty - self.orders_ahead
                self.orders_ahead = 0
                self.fill_my_order(remainder)
        else:
            self.fill_my_order(trade_qty)

    def fill_my_order(self, fill_amount):
        filled = min(self.my_qty, fill_amount)
        self.my_qty -= filled
        print(f"   🎉 I GOT FILLED for {filled} shares! Remaining: {self.my_qty}")
        if self.my_qty <= 0:
            print("   ✅ ORDER COMPLETE.")
            self.is_filled = True

tracker = QueueTracker(my_order_id="ID_123", my_qty=500)

print(f"--- FIFO QUEUE SIMULATION ---")
print(f"My Order: Buy 500. Position in Line: {tracker.orders_ahead}")

trades = [2000, 5000, 2500, 1000] 

for t in trades:
    tracker.process_trade(t)
    if tracker.is_filled: break

print("\nTier 1 Insight: Standard Backtests assume you get filled instantly.")
print("Real HFTs model this Queue Decay to know probability of execution.")