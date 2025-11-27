import heapq

class OrderBook:
    def __init__(self):
        self.asks = [] 
        self.bids = [] 

    def add_limit_order(self, side, price, qty):
        if side == 'ask':
            heapq.heappush(self.asks, (price, qty))
            print(f"📝 ASK PLACED: {qty} @ ₹{price}")
        else:
            heapq.heappush(self.bids, (-price, qty))
            print(f"📝 BID PLACED: {qty} @ ₹{price}")

    def match_market_order(self, side, qty_needed):
        print(f"\n🚀 EXECUTING MARKET {side.upper()} for {qty_needed} units...")
        total_cost = 0
        filled_qty = 0
        
        target_book = self.asks if side == 'buy' else self.bids
        
        while qty_needed > 0 and target_book:
            best_price, available_qty = heapq.heappop(target_book)
            
            if side == 'sell': best_price = -best_price # Flip back for bids
            
            matched = min(qty_needed, available_qty)
            filled_qty += matched
            qty_needed -= matched
            total_cost += (matched * best_price)
            
            print(f"   ⚡ MATCHED {matched} @ ₹{best_price}")
            
            if available_qty > matched:
                new_qty = available_qty - matched
                if side == 'buy': heapq.heappush(target_book, (best_price, new_qty))
                else: heapq.heappush(target_book, (-best_price, new_qty))
                
        avg_price = total_cost / filled_qty if filled_qty > 0 else 0
        print(f"🏁 DONE. Avg Execution Price: ₹{avg_price:.2f}\n")

book = OrderBook()

book.add_limit_order('ask', 101, 50)  
book.add_limit_order('ask', 102, 100) 
book.add_limit_order('ask', 105, 200) 

book.match_market_order('buy', 120)