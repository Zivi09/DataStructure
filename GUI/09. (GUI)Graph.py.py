import tkinter as tk
from tkinter import messagebox, ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualization Tool")
        self.root.geometry("600x600")  # Adjusted window size

        # Configure the root window's grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.graph = nx.Graph()

        # Frame for graph visualization
        self.graph_frame = ttk.LabelFrame(self.root, text="Graph Display", padding=(10, 5))
        self.graph_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Canvas for graph display
        self.fig, self.ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Frame for controls
        self.control_frame = ttk.LabelFrame(self.root, text="Graph Controls", padding=(20, 10))
        self.control_frame.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="ew")

        # Configure grid in control_frame
        self.control_frame.columnconfigure(0, weight=1)
        self.control_frame.columnconfigure(1, weight=2)
        self.control_frame.columnconfigure(2, weight=1)
        
        self.control_frame.rowconfigure(0, weight=1)
        self.control_frame.rowconfigure(1, weight=1)
        self.control_frame.rowconfigure(2, weight=1)
        self.control_frame.rowconfigure(3, weight=1)
        self.control_frame.rowconfigure(4, weight=1)
        self.control_frame.rowconfigure(5, weight=1)

        # Define font size
        font = ('Arial', 13)

        # Add Vertex
        ttk.Label(self.control_frame, text="Vertex:", font=font).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.vertex_entry = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.vertex_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.vertex_button = ttk.Button(self.control_frame, text="Add Vertex", command=self.add_vertex, width=12)
        self.vertex_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Add Edge
        ttk.Label(self.control_frame, text="Edge Vertex 1:", font=font).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.edge_entry1 = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.edge_entry1.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ttk.Label(self.control_frame, text="Edge Vertex 2:", font=font).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.edge_entry2 = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.edge_entry2.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.edge_button = ttk.Button(self.control_frame, text="Add Edge", command=self.add_edge, width=12)
        self.edge_button.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky="ew")

        # Remove Vertex
        ttk.Label(self.control_frame, text="Remove Vertex:", font=font).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.del_vertex_entry = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.del_vertex_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.del_vertex_button = ttk.Button(self.control_frame, text="Remove Vertex", command=self.remove_vertex, width=12)
        self.del_vertex_button.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

        # Remove Edge
        ttk.Label(self.control_frame, text="Edge Vertex 1:", font=font).grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.del_edge_entry1 = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.del_edge_entry1.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        ttk.Label(self.control_frame, text="Edge Vertex 2:", font=font).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.del_edge_entry2 = ttk.Entry(self.control_frame, width=12)  # Decreased width
        self.del_edge_entry2.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        self.del_edge_button = ttk.Button(self.control_frame, text="Remove Edge", command=self.remove_edge, width=12)
        self.del_edge_button.grid(row=4, column=2, rowspan=2, padx=5, pady=5, sticky="ew")

        # Status Label
        self.status_label = ttk.Label(self.root, text="Status: Ready", relief=tk.SUNKEN, anchor="w")
        self.status_label.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # Update the graph display initially
        self.update_graph()

    def update_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=15, font_weight='bold', ax=self.ax)
        self.canvas.draw()
        self.status_label.config(text="Status: Graph Updated")

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            if vertex not in self.graph.nodes:
                self.graph.add_node(vertex)
                self.vertex_entry.delete(0, tk.END)
                self.update_graph()
                self.status_label.config(text=f"Status: Vertex '{vertex}' added.")
            else:
                messagebox.showwarning("Input Error", "Vertex already exists.")
        else:
            messagebox.showerror("Input Error", "Please enter a vertex name.")

    def add_edge(self):
        vertex1 = self.edge_entry1.get()
        vertex2 = self.edge_entry2.get()
        if vertex1 and vertex2:
            if vertex1 in self.graph.nodes and vertex2 in self.graph.nodes:
                if not self.graph.has_edge(vertex1, vertex2):
                    self.graph.add_edge(vertex1, vertex2)
                    self.edge_entry1.delete(0, tk.END)
                    self.edge_entry2.delete(0, tk.END)
                    self.update_graph()
                    self.status_label.config(text=f"Status: Edge '{vertex1}-{vertex2}' added.")
                else:
                    messagebox.showwarning("Input Error", "Edge already exists.")
            else:
                messagebox.showerror("Input Error", "Both vertices must exist.")
        else:
            messagebox.showerror("Input Error", "Please enter both vertex names.")

    def remove_vertex(self):
        vertex = self.del_vertex_entry.get()
        if vertex in self.graph.nodes:
            self.graph.remove_node(vertex)
            self.del_vertex_entry.delete(0, tk.END)
            self.update_graph()
            self.status_label.config(text=f"Status: Vertex '{vertex}' removed.")
        else:
            messagebox.showerror("Input Error", "Vertex does not exist.")

    def remove_edge(self):
        vertex1 = self.del_edge_entry1.get()
        vertex2 = self.del_edge_entry2.get()
        if self.graph.has_edge(vertex1, vertex2):
            self.graph.remove_edge(vertex1, vertex2)
            self.del_edge_entry1.delete(0, tk.END)
            self.del_edge_entry2.delete(0, tk.END)
            self.update_graph()
            self.status_label.config(text=f"Status: Edge '{vertex1}-{vertex2}' removed.")
        else:
            messagebox.showerror("Input Error", "Edge does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
