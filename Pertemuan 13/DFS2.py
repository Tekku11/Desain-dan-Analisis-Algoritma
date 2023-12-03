# Slide 21(Graph)
import networkx as nx
import matplotlib.pyplot as plt
vertices = range(0)
edges = [('Amin','Wasim'),('Amin','Nick'),('Amin','Mike'),('Wasim','Imran'),('Imran','Faras')]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='grey',node_size=1000)
print(nx.betweenness_centrality(G))
plt.show()