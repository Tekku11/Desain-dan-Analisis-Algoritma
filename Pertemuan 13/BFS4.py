# Slide 17
def bfs(graph,start):
  visited=[]
  queue=[]
  queue=[start]
  while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        neighbours = graph[node]
        for neighbour in neighbours:
            queue.append(neighbour)
  return visited

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

print(bfs(graph,'rektor'))