def depth_first_traversal(graph, start_node):
    visited = set()  # Set to track visited nodes

    def dfs(node):
        visited.add(node)
        print(node)  # Process the node (e.g., print its value)

        # Recursive call on adjacent nodes if not visited
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                dfs(adjacent_node)

    # Start the depth-first traversal
    dfs(start_node)
# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the depth-first traversal function
start_node = 'A'
depth_first_traversal(graph, start_node)
