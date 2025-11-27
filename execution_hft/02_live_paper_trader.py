!pip install nselib
!pip install pandas-market-calendars

import pandas as pd
import time
from datetime import datetime
from nselib import capital_market

class PaperBroker:
    def __init__(self, initial_capital=200000): 
        self.capital = initial_capital
        self.positions = [] 
        self.trade_log = [] 

    def get_live_price(self, symbol):
        try:
            data = capital_market.price_volume_and_deliverable_position_data(symbol=symbol, period='1M')
            return float(data['ClosePrice'].iloc[-1].replace(',', ''))
        except:
            return 19500.00 

    def place_order(self, symbol, quantity, side):
        price = self.get_live_price(symbol)
        value = price * quantity

        if side == "BUY":
            if self.capital >= value:
                self.capital -= value
                self.positions.append({'symbol': symbol, 'qty': quantity, 'entry_price': price})
                print(f"✅ BOUGHT {quantity} {symbol} at ₹{price}")
                self.trade_log.append({'time': datetime.now(), 'side': 'BUY', 'price': price})
            else:
                print("❌ Insufficient Funds!")

        elif side == "SELL":
            for pos in self.positions:
                if pos['symbol'] == symbol:
                    profit = (price - pos['entry_price']) * quantity
                    self.capital += (price * quantity)
                    self.positions.remove(pos)
                    print(f"🔻 SOLD {quantity} {symbol} at ₹{price}. P&L: ₹{profit:.2f}")
                    self.trade_log.append({'time': datetime.now(), 'side': 'SELL', 'price': price, 'pnl': profit})
                    return
            print("❌ No position to sell!")

    def show_portfolio(self):
        print(f"💰 Current Cash: ₹{self.capital:.2f} | Open Positions: {len(self.positions)}")

broker = PaperBroker()

print("🚀 Starting Paper Trading Bot...")

for i in range(3): 
    print(f"\n--- Tick {i+1} ---")
    current_price = broker.get_live_price("SBIN")
    print(f"Live SBIN Price: {current_price}")

    if len(broker.positions) == 0:
        broker.place_order("SBIN", 10, "BUY")
    else:
        broker.place_order("SBIN", 10, "SELL")

    broker.show_portfolio()
    time.sleep(2) 