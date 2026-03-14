from collections import deque, defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    def dfs_tree(self, start):
        """Perform DFS and return the Depth-First Tree as a dictionary."""
        visited = set()
        dfs_tree = defaultdict(list)
        stack = [start]
        visited.add(start)
        while stack:
            current = stack.pop()
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs_tree[current].append(neighbor)
                    stack.append(neighbor)
        return dfs_tree
    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
def print_dfs_tree(dfs_tree, start):
    """Print the Depth-First Tree."""
    print(f"Depth-First Tree starting from {start}:")
    for vertex in dfs_tree:
        print(f"{vertex}: {dfs_tree[vertex]}")
if __name__ == "__main__":
    g = Graph()
    for v in ['A', 'B', 'C', 'D', 'E', 'F']:
        g.add_vertex(v)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("Graph:")
    g.display()
    start_vertex = 'A'
    dfs_tree = g.dfs_tree(start_vertex)

    print_dfs_tree(dfs_tree, start_vertex)
