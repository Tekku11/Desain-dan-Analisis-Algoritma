# Slide 29
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Graph
graph = {
            'rektor' : ['warek 1','warek 2'],
            'warek 1' : ['rektor'],
            'warek 2' : ['kaprodi 1','kaprodi 2','kaprodi 3','rektor'],
            'kaprodi 1' : ['dosen A', 'dosen B', 'dosen C', 'warek 2'],
            'kaprodi 2' : ['dosen D','dosen E', 'warek 2'],
            'kaprodi 3': ['dosen F','dosen G', 'warek 2'],
            'dosen G' : ['kaprodi 3'],
            'dosen F' : ['kaprodi 3'],
            'dosen D' : ['kaprodi 2'],
            'dosen E' : ['kaprodi 2'],
            'dosen C' : ['kaprodi 1'],
            'dosen B' : ['kaprodi 1'],
            'dosen A' : ['kaprodi 1']
         }

visited = set()
dfs(visited, graph,'rektor')