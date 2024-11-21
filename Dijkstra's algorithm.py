import heapq


def shortest_path(graph, source):
    
    min_distances = {node: float('infinity') for node in graph}
    min_distances[source] = 0
    pq = [(0, source)]
    prev_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        
        if current_distance > min_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            
            if new_distance < min_distances[neighbor]:
                min_distances[neighbor] = new_distance
                prev_nodes[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    return min_distances, prev_nodes


def reconstruct_path(prev_nodes, source, destination):
    path = []
    node = destination
    while node is not None:
        path.insert(0, node)
        node = prev_nodes[node]
    return path if path[0] == source else None

# First graph example (as adjacency list)
graph_one = {
    'A': [('B', 2), ('D', 4)],
    'B': [('C', 1), ('D', 5)],
    'C': [('E', 3)],
    'D': [('E', 1), ('F', 7)],
    'E': [('F', 2)],
    'F': []
}

# Second graph example
graph_two = {
    '1': [('2', 3), ('3', 6)],
    '2': [('3', 2), ('4', 1)],
    '3': [('4', 4), ('5', 5)],
    '4': [('5', 1)],
    '5': []
}


distances_one, prev_nodes_one = shortest_path(graph_one, 'A')
paths_one = {node: (reconstruct_path(prev_nodes_one, 'A', node), distances_one[node]) for node in graph_one.keys()}


distances_two, prev_nodes_two = shortest_path(graph_two, '1')
paths_two = {node: (reconstruct_path(prev_nodes_two, '1', node), distances_two[node]) for node in graph_two.keys()}

print("Graph One:")
for node, (path, distance) in paths_one.items():
    print(f"Shortest path to {node}: {path}, Distance: {distance}")

print("\nGraph Two:")
for node, (path, distance) in paths_two.items():
    print(f"Shortest path to {node}: {path}, Distance: {distance}")