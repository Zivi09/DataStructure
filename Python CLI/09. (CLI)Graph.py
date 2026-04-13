class Graph:
    def __init__(self):
        # Initialize an empty dictionary to hold the adjacency list
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            print(f"Vertex '{vertex}' added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    def add_edge(self, vertex1, vertex2):
        # Add an edge between two vertices
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 not in self.adj_list[vertex1]:
                self.adj_list[vertex1].append(vertex2)
            if vertex1 not in self.adj_list[vertex2]:
                self.adj_list[vertex2].append(vertex1)
            print(f"Edge between '{vertex1}' and '{vertex2}' added.")
        else:
            print("One or both vertices not found.")

    def remove_vertex(self, vertex):
        # Remove a vertex and all edges connected to it
        if vertex in self.adj_list:
            # Remove the vertex from all other vertex lists
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            # Remove the vertex itself
            del self.adj_list[vertex]
            print(f"Vertex '{vertex}' removed.")
        else:
            print(f"Vertex '{vertex}' does not exist.")

    def remove_edge(self, vertex1, vertex2):
        # Remove an edge between two vertices
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            if vertex2 in self.adj_list[vertex1]:
                self.adj_list[vertex1].remove(vertex2)
            if vertex1 in self.adj_list[vertex2]:
                self.adj_list[vertex2].remove(vertex1)
            print(f"Edge between '{vertex1}' and '{vertex2}' removed.")
        else:
            print("One or both vertices not found.")

    def display_graph(self):
        # Display the adjacency list
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")

def main():
    graph = Graph()

    while True:
        print("\nGraph Operations Menu:")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Remove Vertex")
        print("4. Remove Edge")
        print("5. Display Graph")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vertex = input("Enter vertex to add: ")
            graph.add_vertex(vertex)

        elif choice == '2':
            vertex1 = input("Enter first vertex of the edge: ")
            vertex2 = input("Enter second vertex of the edge: ")
            graph.add_edge(vertex1, vertex2)

        elif choice == '3':
            vertex = input("Enter vertex to remove: ")
            graph.remove_vertex(vertex)

        elif choice == '4':
            vertex1 = input("Enter first vertex of the edge to remove: ")
            vertex2 = input("Enter second vertex of the edge to remove: ")
            graph.remove_edge(vertex1, vertex2)

        elif choice == '5':
            print("Current Graph:")
            graph.display_graph()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
