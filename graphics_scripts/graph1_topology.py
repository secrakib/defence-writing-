import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os

# Ensure graphics directory exists
os.makedirs('e:/Writing Defence/graphics', exist_ok=True)

# Set Elsevier style
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Graph 1: Pivot Translation (Star Topology)
G1 = nx.DiGraph()
dialects = ['Sylheti', 'Chittagonian', 'Barisali', 'Noakhali', 'Mymensingh']
G1.add_node('SCB', pos=(0, 0))
angles = np.linspace(0, 2*np.pi, len(dialects), endpoint=False)
for i, d in enumerate(dialects):
    pos = (np.cos(angles[i]), np.sin(angles[i]))
    G1.add_node(d, pos=pos)
    # Pivot means D -> SCB -> D
    G1.add_edge(d, 'SCB', color='#e74c3c', weight=2, style='solid')
    G1.add_edge('SCB', d, color='#e74c3c', weight=2, style='solid')

pos1 = nx.get_node_attributes(G1, 'pos')
edges1 = G1.edges()
colors1 = [G1[u][v]['color'] for u,v in edges1]
weights1 = [G1[u][v]['weight'] for u,v in edges1]

nx.draw_networkx_nodes(G1, pos1, ax=ax1, node_size=1500, node_color=['#3498db' if n=='SCB' else '#ecf0f1' for n in G1.nodes()], edgecolors='#2c3e50', linewidths=1.5)
nx.draw_networkx_edges(G1, pos1, ax=ax1, edgelist=edges1, edge_color=colors1, width=weights1, arrows=True, arrowsize=15, connectionstyle='arc3,rad=0.1')
nx.draw_networkx_labels(G1, pos1, ax=ax1, font_family='serif', font_size=10, font_weight='bold')

ax1.set_title('Traditional Pivot Translation\n(Cascading Errors)', pad=15)
ax1.axis('off')

# Graph 2: Poly-Dialectal Translation (Fully Connected Mesh)
G2 = nx.DiGraph()
G2.add_node('SCB', pos=(0, 0))
for i, d in enumerate(dialects):
    pos = (np.cos(angles[i]), np.sin(angles[i]))
    G2.add_node(d, pos=pos)

# Connect everything
nodes = list(G2.nodes())
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j:
            G2.add_edge(nodes[i], nodes[j], color='#27ae60', weight=1.0, style='solid')

pos2 = nx.get_node_attributes(G2, 'pos')
edges2 = G2.edges()
colors2 = [G2[u][v]['color'] for u,v in edges2]
weights2 = [G2[u][v]['weight'] for u,v in edges2]

nx.draw_networkx_nodes(G2, pos2, ax=ax2, node_size=1500, node_color=['#3498db' if n=='SCB' else '#ecf0f1' for n in G2.nodes()], edgecolors='#2c3e50', linewidths=1.5)
nx.draw_networkx_edges(G2, pos2, ax=ax2, edgelist=edges2, edge_color=colors2, width=weights2, arrows=True, arrowsize=10, connectionstyle='arc3,rad=0.1', alpha=0.6)
nx.draw_networkx_labels(G2, pos2, ax=ax2, font_family='serif', font_size=10, font_weight='bold')

ax2.set_title('Proposed Poly-Dialectal Translation\n(Direct Unified Mapping)', pad=15)
ax2.axis('off')

plt.tight_layout()
# plt.savefig('e:/Writing Defence/graphics/topology_comparison.pdf', format='pdf', bbox_inches='tight')
print("Saved topology_comparison.pdf")
