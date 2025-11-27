import pandas as pd

portfolio = [
    {'Ticker': 'HDFCBANK', 'Buy_Price': 1700, 'Current_Price': 1750, 'Qty': 100}, 
    {'Ticker': 'INFY',     'Buy_Price': 1600, 'Current_Price': 1400, 'Qty': 100}, 
    {'Ticker': 'TCS',      'Buy_Price': 3500, 'Current_Price': 3600, 'Qty': 50}   
]

substitutes = {
    'INFY': 'WIPRO',     
    'HDFCBANK': 'ICICIBANK'
}

print(f"--- TAX OPTIMIZER ENGINE ---")

total_realized_loss = 0

for pos in portfolio:
    pnl = (pos['Current_Price'] - pos['Buy_Price']) * pos['Qty']
    
    if pnl < -10000:
        print(f"📉 OPPORTUNITY: {pos['Ticker']} is down ₹{abs(pnl)}")
        print(f"   ACTION: SELL {pos['Ticker']} @ {pos['Current_Price']}")
        
        sub = substitutes.get(pos['Ticker'], 'NIFTY_IT_ETF')
        print(f"   ACTION: BUY {sub} (Substitute) to maintain sector exposure.")
        
        total_realized_loss += abs(pnl)
        print(f"   ✅ Tax Loss Booked: ₹{abs(pnl)}")
    else:
        print(f"   HOLD: {pos['Ticker']} (P&L: {pnl})")

print("-" * 40)
print(f"Total Tax Credit Generated: ₹{total_realized_loss}")
print("Insight: This loss offsets your gains in HDFC, lowering your tax bill to ZERO.")