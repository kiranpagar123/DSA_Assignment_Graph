from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def count_trees_in_forest(self):
        visited = set()
        count = 0

        for v in self.vertices:
            if v not in visited:
                self.dfs(v, visited)
                count += 1

        return count

    def dfs(self, v, visited):
        visited.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Create a graph for the forest
graph = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Add edges to represent the connections between nodes
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('E', 'F')
graph.add_edge('G', 'G')

# Count the number of trees in the forest
tree_count = graph.count_trees_in_forest()

# Print the result
print("Number of trees in the forest:", tree_count)
