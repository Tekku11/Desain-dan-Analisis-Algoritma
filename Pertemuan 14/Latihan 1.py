# Slide 29 (Latihan 1)
import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1,11)
edges = [(4,3),(3,2),(3,6),(2,6),(6,5),(6,7),(2,1),(1,7),(7,10),(7,8),(7,9),(9,8)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

# F = Fraud, NF = No Fraud
nx.draw_networkx_nodes(G,pos,nodelist=[1,4,5,7,10],node_color='r',node_size=1300)
nx.draw_networkx_nodes(G,pos,nodelist=[2,3,6,8,9],node_color='g',node_size=1300)
nx.draw_networkx_edges(G,pos,edges,width=3,alpha=0.5,edge_color='b')

labels={}
labels[1]=r'1 F'
labels[2]=r'2 NF'
labels[3]=r'3 NF'
labels[4]=r'4 F'
labels[5]=r'5 F'
labels[6]=r'6 NF'
labels[7]=r'7 F'
labels[8]=r'8 NF'
labels[9]=r'9 NF'
labels[10]=r'10 F'
nx.draw_networkx_labels(G,pos,labels,font_size=16)
plt.show()
