from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def is_cyclic_util(self, v, visited, recursion_stack):
        visited.add(v)
        recursion_stack.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(v)
        return False

    def is_cyclic(self):
        visited = set()
        recursion_stack = set()

        for v in range(self.num_vertices):
            if v not in visited:
                if self.is_cyclic_util(v, visited, recursion_stack):
                    return True

        return False
# Create a graph
graph = Graph(4)

# Add edges to represent the connections between vertices
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Check if the graph contains any cycles
has_cycle = graph.is_cyclic()

# Print the result
if has_cycle:
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
