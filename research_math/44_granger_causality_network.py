import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

np.random.seed(42)
n = 1000

bank_nifty = np.random.randn(n)

nifty_it = np.roll(bank_nifty, 1) + np.random.randn(n) * 0.5

data = pd.DataFrame({'BankNifty': bank_nifty, 'NiftyIT': nifty_it})

maxlag = 2
test = 'ssr_chi2test'

print("--- CAUSALITY TEST: Does BankNifty lead NiftyIT? ---")
results = grangercausalitytests(data[['NiftyIT', 'BankNifty']], maxlag=maxlag, verbose=False)

for lag in range(1, maxlag+1):
    p_value = results[lag][0][test][1]
    print(f"Lag {lag}: P-Value = {p_value:.5f}")
    if p_value < 0.05:
        print(f"   ✅ CAUSALITY CONFIRMED at Lag {lag}")
    else:
        print(f"   ❌ NO CAUSALITY")

print("\n--- REVERSE TEST: Does NiftyIT lead BankNifty? ---")
results_reverse = grangercausalitytests(data[['BankNifty', 'NiftyIT']], maxlag=maxlag, verbose=False)

for lag in range(1, maxlag+1):
    p_value = results_reverse[lag][0][test][1]
    print(f"Lag {lag}: P-Value = {p_value:.5f}")