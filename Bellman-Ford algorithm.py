def bellman_ford(graph, source):

    min_costs = {node: float('infinity') for node in graph}
    min_costs[source] = 0
    prev_nodes = {node: None for node in graph}


    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if min_costs[node] + weight < min_costs[neighbor]:
                    min_costs[neighbor] = min_costs[node] + weight
                    prev_nodes[neighbor] = node

    
    for node in graph:
        for neighbor, weight in graph[node]:
            if min_costs[node] + weight < min_costs[neighbor]:
                raise ValueError("Negative weight cycle detected in the graph.")

    return min_costs, prev_nodes

def trace_path(prev_nodes, source, destination):
    path = []
    current_node = destination
    while current_node is not None:
        path.insert(0, current_node)
        current_node = prev_nodes[current_node]
    return path if path[0] == source else None

graph_a = {
    'S': [('A', 4), ('B', 2)],
    'A': [('C', 3), ('B', 1)],
    'B': [('D', 2)],
    'C': [('D', -5)],
    'D': [('E', 2)],
    'E': []
}

graph_b = {
    'X': [('Y', 6), ('Z', 5)],
    'Y': [('W', -4)],
    'Z': [('Y', -2), ('W', 3)],
    'W': [('X', -3)],
}

try:
    costs_a, predecessors_a = bellman_ford(graph_a, 'S')
    paths_a = {node: (trace_path(predecessors_a, 'S', node), costs_a[node]) for node in graph_a.keys()}
except ValueError as e:
    paths_a = str(e)

try:
    costs_b, predecessors_b = bellman_ford(graph_b, 'X')
    paths_b = {node: (trace_path(predecessors_b, 'X', node), costs_b[node]) for node in graph_b.keys()}
except ValueError as e:
    paths_b = str(e)

print("Graph A:")
if isinstance(paths_a, str):
    print(paths_a)
else:
    for node, (path, cost) in paths_a.items():
        print(f"Shortest path to {node}: {path}, Cost: {cost}")

print("\nGraph B:")
if isinstance(paths_b, str):
    print(paths_b)
else:
    for node, (path, cost) in paths_b.items():
        print(f"Shortest path to {node}: {path}, Cost: {cost}")

### output
Graph A:
Shortest path to S: ['S'], Cost: 0
Shortest path to A: ['S', 'A'], Cost: 4
Shortest path to B: ['S', 'B'], Cost: 2
Shortest path to C: ['S', 'A', 'C'], Cost: 7
Shortest path to D: ['S', 'A', 'C', 'D'], Cost: 2
Shortest path to E: ['S', 'A', 'C', 'D', 'E'], Cost: 4

Graph B:
Negative weight cycle detected in the graph.
###
