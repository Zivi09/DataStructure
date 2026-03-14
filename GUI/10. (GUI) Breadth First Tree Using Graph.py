import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class BFS_Graph:
    def __init__(self, master):
        self.master = master
        master.title("Breadth-First Search Graph")

        # Create input fields for graph nodes and edges
        self.node_label = tk.Label(master, text="Enter nodes (comma separated):")
        self.node_label.pack()
        self.node_entry = tk.Entry(master, width=50)
        self.node_entry.pack()

        self.edge_label = tk.Label(master, text="Enter edges (node1,node2;node3,node4;...):")
        self.edge_label.pack()
        self.edge_entry = tk.Entry(master, width=50)
        self.edge_entry.pack()

        # Create input fields for start and end points
        self.start_label = tk.Label(master, text="Enter start point:")
        self.start_label.pack()
        self.start_entry = tk.Entry(master, width=20)
        self.start_entry.pack()

        self.end_label = tk.Label(master, text="Enter end point:")
        self.end_label.pack()
        self.end_entry = tk.Entry(master, width=20)
        self.end_entry.pack()

        # Create button to generate graph and perform BFS
        self.generate_button = tk.Button(master, text="Generate Graph and Perform BFS", command=self.generate_graph)
        self.generate_button.pack()

    def generate_graph(self):
        # Get user input for nodes and edges
        nodes = [node.strip() for node in self.node_entry.get().split(',')]
        edges_input = self.edge_entry.get()

        # Check if edges input is valid
        edges = []
        for edge in edges_input.split(';'):
            edge_parts = edge.split(',')
            if len(edge_parts) != 2:
                messagebox.showerror("Invalid input", "Edges must be entered in the format node1,node2;node3,node4;...")
                return
            edges.append((edge_parts[0].strip(), edge_parts[1].strip()))

        # Get user input for start and end points
        start_point = self.start_entry.get().strip()
        end_point = self.end_entry.get().strip()

        # Create graph using NetworkX
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        # Perform BFS traversal
        try:
            bfs_traversal = nx.shortest_path(G, source=start_point, target=end_point)
            bfs_distance = nx.shortest_path_length(G, source=start_point, target=end_point)
        except nx.NetworkXNoPath:
            bfs_traversal = "No path found from {} to {}".format(start_point, end_point)
            bfs_distance = "N/A"

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

        # Draw original graph on the left subplot
        pos = nx.spring_layout(G)  # Use spring layout to position nodes
        nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12, ax=ax1)
        ax1.set_title("Original Graph")

        # Draw BFS graph on the right subplot
        bfs_G = nx.Graph()
        bfs_G.add_nodes_from(bfs_traversal)
        bfs_G.add_edges_from([(bfs_traversal[i], bfs_traversal[i+1]) for i in range(len(bfs_traversal)-1)])
        pos = nx.spring_layout(bfs_G)  # Use spring layout to position nodes
        nx.draw_networkx(bfs_G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12, ax=ax2)
        ax2.set_title("BFS Traversal")
        ax2.set_xlabel("Shortest distance: {}".format(bfs_distance))

        # Use a smaller font size for node labels to prevent them from being cut off
        for text in ax1.texts + ax2.texts:
            text.set_fontsize(10)

        plt.show()

root = tk.Tk()
my_gui = BFS_Graph(root)
root.mainloop()