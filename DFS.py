
graph={
    
    'A':['B','C','D'],
    'B':['A'],
    'C':['A','D'],
    'D':['A','C','E'],
    'E':['D']
}


visited = set() 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
 