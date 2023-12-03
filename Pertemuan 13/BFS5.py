import networkx as nx
import matplotlib.pyplot as plt
vertices = range(0)
edges = [('Rektor','Warek 1'),('Rektor','Warek 2'),
         ('Warek 2','Kaprodi 1'),('Warek 2', 'Kaprodi 2'),('Warek 2','Kaprodi 3'),
         ('Kaprodi 1', 'Dosen A'),('Kaprodi 1', 'Dosen B'),('Kaprodi 1', 'Dosen C'),
         ('Kaprodi 2', 'Dosen D'),('Kaprodi 2', 'Dosen E'),
         ('Kaprodi 3', 'Dosen F'),('Kaprodi 3', 'Dosen G')
         ]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True,node_color='g',node_size=1000)
print(nx.betweenness_centrality(G))
plt.show()