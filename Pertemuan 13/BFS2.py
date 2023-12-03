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

# Slide 6
graph = {
            '0' : ['9','7','11'],
            '9' : ['8','10','0'],
            '7' : ['6','3','0','11'],
            '8' : ['1','12','9'],
            '6' : ['5','7'],
            '12': ['2','8'],
            '3' : ['2','4','7'],
            '5' : ['6'],
            '4' : ['3'],
            '1' : ['10','8'],
            '2' : ['3','12'],
            '10' : ['9','1'],
            '11' : ['9','7']
         }

print(bfs(graph,'0'))