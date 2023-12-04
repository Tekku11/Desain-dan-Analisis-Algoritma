# Slide 30 (Latihan 2)
import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1,13)
edges = [(13,12),(12,11),(12,2),(12,3),(11,3),(11,10),(10,3),(2,3),(2,1),(1,3),(3,4),(4,7),(4,5),(4,6),(6,5),(6,9),(7,5),(7,8),(9,8),(8,5)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

# F = Fraud, NF = No Fraud
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,10,11,12],node_color='r',node_size=700)
nx.draw_networkx_nodes(G,pos,nodelist=[4,5,6,7,8,9,13],node_color='g',node_size=700)
nx.draw_networkx_edges(G,pos,edges,width=3,alpha=1,edge_color='blue')

labels={}
labels[1]=r'1 F'
labels[2]=r'2 F'
labels[3]=r'3 F'
labels[4]=r'4 NF'
labels[5]=r'5 NF'
labels[6]=r'6 NF'
labels[7]=r'7 NF'
labels[8]=r'8 NF'
labels[9]=r'9 NF'
labels[10]=r'10 F'
labels[11]=r'11 F'
labels[12]=r'12 F'
labels[13]=r'13 NF'
nx.draw_networkx_labels(G,pos,labels,font_size=16)
plt.show()
