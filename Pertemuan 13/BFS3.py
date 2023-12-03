# Slide 6
import networkx as nx
import matplotlib.pyplot as plt
vertices = range(0,13)
edges = [(0,9),(0,11),(0,7),(11,7),(9,8),(9,10),(10,1),(1,8),(8,12),(12,2),(2,3),(3,4),(3,7),(7,6),(6,5)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='y',node_size=1000)
print(nx.betweenness_centrality(G))
plt.show()