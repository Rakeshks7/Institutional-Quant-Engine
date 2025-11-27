import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node("TSMC", sector="Semiconductors", exposure=1.0) 
G.add_node("Foxconn", sector="Manufacturing", exposure=0.0)
G.add_node("Apple", sector="Consumer Elec", exposure=0.0)
G.add_node("BestBuy", sector="Retail", exposure=0.0)
G.add_node("Nvidia", sector="Chips", exposure=0.0)

G.add_edge("TSMC", "Apple", weight=0.4)   
G.add_edge("TSMC", "Nvidia", weight=0.8)  
G.add_edge("TSMC", "Foxconn", weight=0.3)
G.add_edge("Foxconn", "Apple", weight=0.6)
G.add_edge("Apple", "BestBuy", weight=1.0) 

initial_shock = -0.5
impact_scores = {"TSMC": initial_shock}

print("--- SUPPLY CHAIN SHOCKWAVE ---")
print(f"Event: Earthquake at TSMC (Severity {initial_shock})")

for node in nx.topological_sort(G):
    if node == "TSMC": continue
    
    total_impact = 0
    predecessors = list(G.predecessors(node))
    
    for pred in predecessors:
        weight = G[pred][node]['weight']
        pred_impact = impact_scores.get(pred, 0)
        passed_impact = pred_impact * weight
        total_impact += passed_impact
        
    impact_scores[node] = total_impact
    print(f"📉 {node} Impact: {total_impact:.4f} (Derived from {predecessors})")

print("\n--- ALGO EXECUTION ---")
for company, impact in impact_scores.items():
    if impact < -0.1:
        print(f"SHORT {company} (Predicted drop before news)")