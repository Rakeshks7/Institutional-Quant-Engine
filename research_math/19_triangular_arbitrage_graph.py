import networkx as nx
import math

rates = {
    ('USD', 'INR'): 83.00,
    ('INR', 'EUR'): 0.011, 
    ('EUR', 'USD'): 1.10   
}


G = nx.DiGraph()

for (src, dst), rate in rates.items():
    weight = -math.log(rate)
    G.add_edge(src, dst, weight=weight)
    print(f"Edge {src}->{dst} : Rate {rate} | Weight {weight:.4f}")


try:
    cycle = nx.find_negative_cycle(G, source='USD')
    print("\n🚨 ARBITRAGE DETECTED! (Negative Cycle Found)")
    print(f"Path: {cycle}")
    
    profit = 1.0
    for i in range(len(cycle)-1):
        u, v = cycle[i], cycle[i+1]
        if (u,v) in rates: rate = rates[(u,v)]
        else: rate = 1/rates[(v,u)] 
        profit *= rate
        
    print(f"Starting with 1.0 unit -> Ending with {profit:.5f} units")
    print(f"ROI: {(profit-1)*100:.4f}% (Risk Free)")

except nx.NetworkXNoCycle:
    print("No Arbitrage Opportunity found.")