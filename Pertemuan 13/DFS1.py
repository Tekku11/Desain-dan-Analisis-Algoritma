# Slide 21 (DEPTH-FIRST SEARCH)
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Slide 22
graph = {'Amin'      : ['Wasim','Nick','Mike'],
         'Wasim'     : ['Imran','Amin'],
         'Imran'     : ['Wasim','Faras'],
         'Faras'     : ['Imran'],
         'Mike'      : ['Amin'],
         'Nick'      : ['Amin']
         }

# Slide 24
visited = set()
dfs(visited, graph, 'Amin')
