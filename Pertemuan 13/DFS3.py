# Slide 20
import networkx as nx
import matplotlib.pyplot as plt
vertices = range(0)
edges = [(0,1),(0,9),(1,8),(9,8),(8,7),(7,10),(10,11),(11,7),(7,6),(7,3),
         (6,5),(5,3),(3,4),(3,2)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='grey',node_size=1000)
print(nx.betweenness_centrality(G))
plt.show()