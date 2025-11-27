import queue
import pandas as pd

class Event:
    pass

class MarketEvent(Event):
    def __init__(self): self.type = 'MARKET'

class SignalEvent(Event):
    def __init__(self, symbol, datetime, signal_type):
        self.type = 'SIGNAL'
        self.symbol = symbol
        self.datetime = datetime
        self.signal_type = signal_type 

class OrderEvent(Event):
    def __init__(self, symbol, order_type, quantity, direction):
        self.type = 'ORDER'
        self.symbol = symbol
        self.qty = quantity
        self.direction = direction 

class BacktestEngine:
    def __init__(self):
        self.events = queue.Queue() 
        self.portfolio = {'CASH': 100000, 'HOLDINGS': {}}
    
    def run(self, data_feed):
        print("⚙️ STARTING EVENT-DRIVEN ENGINE...")
        
        for index, row in data_feed.iterrows():
            self.events.put(MarketEvent())
            
            if row['Close'] > 105: 
                self.events.put(SignalEvent('ASSET', index, 'LONG'))
            
            while True:
                try:
                    event = self.events.get(False)
                except queue.Empty:
                    break
                
                if event.type == 'MARKET':
                    pass 
                
                elif event.type == 'SIGNAL':
                    print(f"[{event.datetime}] 📡 SIGNAL RECEIVED: {event.signal_type}")
                    self.events.put(OrderEvent(event.symbol, 'MKT', 100, 'BUY'))
                    
                elif event.type == 'ORDER':
                    print(f"   🛒 EXECUTING ORDER: {event.direction} {event.qty} units")
                    self.portfolio['HOLDINGS']['ASSET'] = 100
                    self.portfolio['CASH'] -= 10500 

dates = pd.date_range(start='2024-01-01', periods=5)
data = pd.DataFrame({'Close': [100, 102, 106, 104, 108]}, index=dates)

engine = BacktestEngine()
engine.run(data)