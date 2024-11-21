def shortest_paths(matrix):
    
    size = len(matrix)
    cost = [[matrix[row][col] for col in range(size)] for row in range(size)]
    successor = [[None if matrix[row][col] == float('inf') else col for col in range(size)] for row in range(size)]

    for mid in range(size):
        for src in range(size):
            for dest in range(size):
                if cost[src][mid] + cost[mid][dest] < cost[src][dest]:
                    cost[src][dest] = cost[src][mid] + cost[mid][dest]
                    successor[src][dest] = successor[src][mid]

    return cost, successor

def retrieve_path(successor, start, end):
    if successor[start][end] is None:
        return None
    route = [start]
    while start != end:
        start = successor[start][end]
        route.append(start)
    return route

graph_1 = [
    [0, 2, float('inf'), 1, float('inf')],
    [float('inf'), 0, 3, float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, 4, 5],
    [float('inf'), float('inf'), 1, 0, float('inf')],
    [3, float('inf'), float('inf'), float('inf'), 0]
]

graph_2 = [
    [0, 7, float('inf'), 2],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [6, float('inf'), 4, 0]
]

distances_1, paths_1 = shortest_paths(graph_1)
distances_2, paths_2 = shortest_paths(graph_2)

paths_graph1 = {}
for a in range(len(graph_1)):
    for b in range(len(graph_1)):
        paths_graph1[(a, b)] = retrieve_path(paths_1, a, b)

paths_graph2 = {}
for a in range(len(graph_2)):
    for b in range(len(graph_2)):
        paths_graph2[(a, b)] = retrieve_path(paths_2, a, b)

print("Graph 1 - Shortest Distance Matrix:")
for row in distances_1:
    print(row)

print("\nGraph 1 - Paths:")
for (start, end), route in paths_graph1.items():
    print(f"Path from {start} to {end}: {route}")

print("\nGraph 2 - Shortest Distance Matrix:")
for row in distances_2:
    print(row)

print("\nGraph 2 - Paths:")
for (start, end), route in paths_graph2.items():
    print(f"Path from {start} to {end}: {route}")
### output
Graph 1 - Shortest Distance Matrix:
[0, 2, 2, 1, 7]
[11, 0, 3, 7, 8]
[8, 10, 0, 4, 5]
[9, 11, 1, 0, 6]
[3, 5, 5, 4, 0]

Graph 1 - Paths:
Path from 0 to 0: [0]
Path from 0 to 1: [0, 1]
Path from 0 to 2: [0, 3, 2]
Path from 0 to 3: [0, 3]
Path from 0 to 4: [0, 3, 2, 4]
Path from 1 to 0: [1, 2, 4, 0]
Path from 1 to 1: [1]
Path from 1 to 2: [1, 2]
Path from 1 to 3: [1, 2, 3]
Path from 1 to 4: [1, 2, 4]
Path from 2 to 0: [2, 4, 0]
Path from 2 to 1: [2, 4, 0, 1]
Path from 2 to 2: [2]
Path from 2 to 3: [2, 3]
Path from 2 to 4: [2, 4]
Path from 3 to 0: [3, 2, 4, 0]
Path from 3 to 1: [3, 2, 4, 0, 1]
Path from 3 to 2: [3, 2]
Path from 3 to 3: [3]
Path from 3 to 4: [3, 2, 4]
Path from 4 to 0: [4, 0]
Path from 4 to 1: [4, 0, 1]
Path from 4 to 2: [4, 0, 3, 2]
Path from 4 to 3: [4, 0, 3]
Path from 4 to 4: [4]

Graph 2 - Shortest Distance Matrix:
[0, 7, 6, 2]
[12, 0, 5, 6]
[7, 14, 0, 1]
[6, 13, 4, 0]

Graph 2 - Paths:
Path from 0 to 0: [0]
Path from 0 to 1: [0, 1]
Path from 0 to 2: [0, 3, 2]
Path from 0 to 3: [0, 3]
Path from 1 to 0: [1, 2, 3, 0]
Path from 1 to 1: [1]
Path from 1 to 2: [1, 2]
Path from 1 to 3: [1, 2, 3]
Path from 2 to 0: [2, 3, 0]
Path from 2 to 1: [2, 3, 0, 1]
Path from 2 to 2: [2]
Path from 2 to 3: [2, 3]
Path from 3 to 0: [3, 0]
Path from 3 to 1: [3, 0, 1]
Path from 3 to 2: [3, 2]
Path from 3 to 3: [3]
###
