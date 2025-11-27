import networkx as nx
import matplotlib.pyplot as plt

trades = [
    ('Trader_A', 'Trader_B', 100, '10:00:01'),
    ('Trader_B', 'Trader_C', 100, '10:00:05'),
    ('Trader_C', 'Trader_D', 50,  '10:00:10'), 
    ('Trader_C', 'Trader_A', 100, '10:00:15')  
]

G = nx.DiGraph()

for seller, buyer, qty, time in trades:
    G.add_edge(seller, buyer, weight=qty, timestamp=time)

try:
    cycles = list(nx.simple_cycles(G))
    wash_trades = [c for c in cycles if len(c) > 1] 

    print(f"--- SURVEILLANCE ALERT ---")
    if wash_trades:
        print("🚨 WASH TRADING RING DETECTED!")
        for ring in wash_trades:
            print(f"   Participants: {ring}")
            print(f"   Action: Freezing accounts {ring} immediately.")
    else:
        print("✅ No market manipulation detected.")
except Exception as e:
    print(f"An error occurred during wash trade detection: {e}")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='red', node_size=2000, font_color='white')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v): d['weight'] for u,v,d in G.edges(data=True)}) 
plt.title('RegTech: Detecting Collusion Rings')
plt.show()

print("Tier 1 Insight: Regulators use this Graph Theory to catch 'Pump and Dump' schemes.")