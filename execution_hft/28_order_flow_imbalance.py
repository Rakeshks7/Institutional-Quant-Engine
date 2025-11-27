import pandas as pd
import numpy as np

data = {
    'Best_Bid_Qty': [100, 120, 120, 80, 50],
    'Best_Bid_Px':  [100, 100, 101, 101, 101],
    'Best_Ask_Qty': [100, 100, 80, 150, 200],
    'Best_Ask_Px':  [101, 101, 102, 102, 102]
}
df = pd.DataFrame(data)


def calculate_ofi(row, prev_row):
    ofi = 0
    
    if row['Best_Bid_Px'] > prev_row['Best_Bid_Px']:
        ofi += row['Best_Bid_Qty'] 
    elif row['Best_Bid_Px'] == prev_row['Best_Bid_Px']:
        ofi += (row['Best_Bid_Qty'] - prev_row['Best_Bid_Qty']) 
    else:
        ofi -= row['Best_Bid_Qty'] 
        
    if row['Best_Ask_Px'] > prev_row['Best_Ask_Px']:
        ofi += row['Best_Ask_Qty'] 
    elif row['Best_Ask_Px'] == prev_row['Best_Ask_Px']:
        ofi -= (row['Best_Ask_Qty'] - prev_row['Best_Ask_Qty'])
    else:
        ofi -= row['Best_Ask_Qty'] 
        
    return ofi

ofi_stream = []
for i in range(1, len(df)):
    val = calculate_ofi(df.iloc[i], df.iloc[i-1])
    ofi_stream.append(val)

print("--- ORDER FLOW IMBALANCE (OFI) STREAM ---")
print(f"OFI Values: {ofi_stream}")
print("Positive = Buy Pressure | Negative = Sell Pressure")
print("HFT Algos trade purely based on this number, ignoring the actual price.")