# Slide 28
import networkx as nx
import matplotlib.pyplot as plt

# Hembuat graph (jaringan sosial)
G = nx.Graph()

# Menambahkan vertices dan edges
vertices = range(1, 10)
edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,6), (1,7), (2,8), (2,9)]
G.add_nodes_from(vertices)
G.add_edges_from(edges)

# Menghitung derajat setiap node
degree_values = dict(G.degree())

# DOS values (derajat tanpa normalisasi)
dos_values = {node: degree for node, degree in degree_values.items()}

# Menampilkan DOS values
print("DOS values:")
for node, dos in dos_values.items():
    print(f"{node} : {dos}")

# Normalisasi nilai derajat ke dalam rentang 0-9 
max_degree = max(degree_values.values())

#Menghitung DoS values (derajat yang dinormalisasi)
normalized_dos_values = {node: round((degree / max_degree) * 9, 2) for node, degree in degree_values.items()}

# Menampilkan DOS values (derajat yang dinormalisasi)
print("\nNormalized DOS values:")
for node, normalized_dos in normalized_dos_values.items():
    print(f"{node}: {normalized_dos}")
