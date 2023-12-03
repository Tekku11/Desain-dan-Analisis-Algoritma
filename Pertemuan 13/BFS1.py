# Slide 10
def bfs(graph,start):
    visited = []
    queue = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
              visited.append(node)
              neighbours = graph[node]
              for neighbour in neighbours:
                     queue.append(neighbour)
    return visited

#----------------------------------------------------------------
# Slide 11
graph = {'Amin'      : ['Wasim','Nick','Mike'],
         'Wasim'     : ['Imran','Amin'],
         'Imran'     : ['Wasim','Faras'],
         'Faras'     : ['Imran'],
         'Mike'      : ['Amin'],
         'Nick'      : ['Amin']
         }

#----------------------------------------------------------------
# Slide 12
print(bfs(graph,'Amin'))
'''
print(bfs(graph,'Wasim'))
print(bfs(graph,'Faras'))
'''