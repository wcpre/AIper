graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

def dls(graph, node, goal, depth_limit, current_depth=0):
    if current_depth > depth_limit:
        return False
        
    print(node, end="  ")

    if node == goal:
        return True  
        
    for neighbour in graph[node]:
        if dls(graph, neighbour, goal, depth_limit, current_depth + 1):
            return True

    return False

limit = 2
goal_node = 'B'
print("DLS With depth limit {}:".format(limit))
found = dls(graph, 'A', goal_node, limit)

if found:
    print("\nGoal node '{}' found within depth limit.".format(goal_node))
else:
    print("\nGoal node '{}' not found within depth limit.".format(goal_node))