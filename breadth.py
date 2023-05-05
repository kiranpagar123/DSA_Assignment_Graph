from collections import deque

def breadth_first_traversal(graph, start_node):
    visited = set()  # Set to track visited nodes
    queue = deque()  # Queue for BFS

    # Enqueue the start node
    queue.append(start_node)
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node)  # Process the node (e.g., print its value)

        # Enqueue adjacent nodes if not visited
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
                visited.add(adjacent_node)
# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the breadth-first traversal function
start_node = 'A'
breadth_first_traversal(graph, start_node)
