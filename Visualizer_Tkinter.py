import tkinter as tk
from tkinter import messagebox
from collections import defaultdict, Counter
import heapq
import itertools
import math
import random

# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Stack GUI
class StackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stack")
        self.master.configure(bg="lightblue")

        self.stack = Stack()

        # Canvas for stack visualization
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        # Input and buttons
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.push_button = tk.Button(master, text="Push", command=self.push, bg="lightgreen")
        self.push_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.pop_button = tk.Button(master, text="Pop", command=self.pop, bg="salmon")
        self.pop_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.peek_button = tk.Button(master, text="Peek", command=self.peek, bg="lightyellow")
        self.peek_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.is_empty_button = tk.Button(master, text="isEmpty", command=self.is_empty, bg="lightpink")
        self.is_empty_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.size_button = tk.Button(master, text="Size", command=self.size, bg="lightcyan")
        self.size_button.pack(side=tk.LEFT, padx=10, pady=5)

    def update_canvas(self):
        self.canvas.delete("all")
        for i, item in enumerate(reversed(self.stack.items)):
            self.canvas.create_rectangle(50, 50 + i * 30, 250, 80 + i * 30, fill="lightgray")
            self.canvas.create_text(150, 65 + i * 30, text=item, font=("Arial", 16))

    def push(self):
        item = self.entry.get()
        if item:
            self.stack.push(item)
            self.entry.delete(0, tk.END)
            self.update_canvas()

    def pop(self):
        item = self.stack.pop()
        if item is None:
            messagebox.showinfo("Info", "Stack is empty!")
        else:
            self.update_canvas()

    def peek(self):
        item = self.stack.peek()
        messagebox.showinfo("Info", f"Top item: {item}" if item else "Stack is empty!")

    def is_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Info", "Stack is empty!")
        else:
            messagebox.showinfo("Info", "Stack is not empty.")

    def size(self):
        size = self.stack.size()
        messagebox.showinfo("Info", f"Stack size: {size}")


# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Queue GUI
class QueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Queue")
        self.master.configure(bg="lightgreen")

        self.queue = Queue()

        # Canvas for queue visualization
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        # Input and buttons
        self.enqueue_entry = tk.Entry(master)
        self.enqueue_entry.pack(pady=5)

        self.enqueue_button = tk.Button(master, text="Enqueue", command=self.enqueue, bg="lightblue")
        self.enqueue_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.dequeue_button = tk.Button(master, text="Dequeue", command=self.dequeue, bg="salmon")
        self.dequeue_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.is_empty_button = tk.Button(master, text="isEmpty", command=self.is_empty, bg="lightpink")
        self.is_empty_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.size_button = tk.Button(master, text="Size", command=self.size, bg="lightcyan")
        self.size_button.pack(side=tk.LEFT, padx=10, pady=5)

    def update_canvas(self):
        self.canvas.delete("all")
        for i, item in enumerate(self.queue.items):
            self.canvas.create_rectangle(50, 50 + i * 30, 250, 80 + i * 30, fill="lightgray")
            self.canvas.create_text(150, 65 + i * 30, text=item, font=("Arial", 16))

    def enqueue(self):
        item = self.enqueue_entry.get()
        if item:
            self.queue.enqueue(item)
            self.enqueue_entry.delete(0, tk.END)
            self.update_canvas()

    def dequeue(self):
        item = self.queue.dequeue()
        if item is None:
            messagebox.showinfo("Info", "Queue is empty!")
        else:
            self.update_canvas()

    def is_empty(self):
        if self.queue.is_empty():
            messagebox.showinfo("Info", "Queue is empty!")
        else:
            messagebox.showinfo("Info", "Queue is not empty.")

    def size(self):
        size = self.queue.size()
        messagebox.showinfo("Info", f"Queue size: {size}")


# Doubly Linked List Implementation
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Move head if needed
                    self.head = current.next
                return
            current = current.next

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Doubly Linked List GUI
class DoublyLinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Doubly Linked List")
        self.master.configure(bg="lightpink")

        self.dll = DoublyLinkedList()

        # Canvas for visualization
        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Input and buttons
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.insert_button = tk.Button(master, text="Insert", command=self.insert, bg="lightgreen")
        self.insert_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete, bg="salmon")
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse, bg="lightyellow")
        self.traverse_button.pack(side=tk.LEFT, padx=10, pady=5)

    def update_canvas(self):
        self.canvas.delete("all")
        current = self.dll.head
        x_start = 50
        while current:
            self.canvas.create_rectangle(x_start, 100, x_start + 50, 150, fill="lightgray")
            self.canvas.create_text(x_start + 25, 125, text=current.data, font=("Arial", 16))
            x_start += 60
            current = current.next

    def insert(self):
        data = self.entry.get()
        if data:
            self.dll.insert(data)
            self.entry.delete(0, tk.END)
            self.update_canvas()

    def delete(self):
        data = self.entry.get()
        if data:
            self.dll.delete(data)
            self.entry.delete(0, tk.END)
            self.update_canvas()

    def traverse(self):
        elements = self.dll.traverse()
        messagebox.showinfo("Traverse", f"Doubly Linked List: {elements}")


# Priority Queue Implementation
class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.items.sort()

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Priority Queue GUI
class PriorityQueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Priority Queue")
        self.master.configure(bg="lightcyan")

        self.priority_queue = PriorityQueue()

        # Canvas for visualization
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        # Input and buttons
        self.enqueue_entry = tk.Entry(master)
        self.enqueue_entry.pack(pady=5)

        self.enqueue_button = tk.Button(master, text="Enqueue", command=self.enqueue, bg="lightblue")
        self.enqueue_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.dequeue_button = tk.Button(master, text="Dequeue", command=self.dequeue, bg="salmon")
        self.dequeue_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.is_empty_button = tk.Button(master, text="isEmpty", command=self.is_empty, bg="lightpink")
        self.is_empty_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.size_button = tk.Button(master, text="Size", command=self.size, bg="lightcyan")
        self.size_button.pack(side=tk.LEFT, padx=10, pady=5)

    def update_canvas(self):
        self.canvas.delete("all")
        for i, item in enumerate(self.priority_queue.items):
            self.canvas.create_rectangle(50, 50 + i * 30, 250, 80 + i * 30, fill="lightgray")
            self.canvas.create_text(150, 65 + i * 30, text=item, font=("Arial", 16))

    def enqueue(self):
        item = self.enqueue_entry.get()
        if item:
            self.priority_queue.enqueue(item)
            self.enqueue_entry.delete(0, tk.END)
            self.update_canvas()

    def dequeue(self):
        item = self.priority_queue.dequeue()
        if item is None:
            messagebox.showinfo("Info", "Priority Queue is empty!")
        else:
            self.update_canvas()

    def is_empty(self):
        if self.priority_queue.is_empty():
            messagebox.showinfo("Info", "Priority Queue is empty!")
        else:
            messagebox.showinfo("Info", "Priority Queue is not empty.")

    def size(self):
        size = self.priority_queue.size()
        messagebox.showinfo("Info", f"Priority Queue size: {size}")


# Binary Tree Implementation
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if not node.right:
                node.right = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def traverse_in_order(self):
        elements = []
        self._traverse_in_order_recursive(self.root, elements)
        return elements

    def _traverse_in_order_recursive(self, node, elements):
        if node:
            self._traverse_in_order_recursive(node.left, elements)
            elements.append(node.data)
            self._traverse_in_order_recursive(node.right, elements)


# Binary Tree GUI
class BinaryTreeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Tree")
        self.master.configure(bg="lightyellow")

        self.binary_tree = BinaryTree()

        # Canvas for visualization
        self.canvas = tk.Canvas(master, width=500, height=300, bg="white")
        self.canvas.pack()

        # Input and buttons
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.insert_button = tk.Button(master, text="Insert", command=self.insert, bg="lightgreen")
        self.insert_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.traverse_button = tk.Button(master, text="Traverse In-Order", command=self.traverse_in_order, bg="lightblue")
        self.traverse_button.pack(side=tk.LEFT, padx=10, pady=5)

    def update_canvas(self):
        self.canvas.delete("all")
        self._draw_tree(self.binary_tree.root, 250, 50, 100)

    def _draw_tree(self, node, x, y, offset):
        if node:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightgray")
            self.canvas.create_text(x, y, text=node.data, font=("Arial", 12))
            if node.left:
                self.canvas.create_line(x, y, x - offset, y + 50)
                self._draw_tree(node.left, x - offset, y + 50, offset // 2)
            if node.right:
                self.canvas.create_line(x, y, x + offset, y + 50)
                self._draw_tree(node.right, x + offset, y + 50, offset // 2)

    def insert(self):
        data = self.entry.get()
        if data:
            self.binary_tree.insert(data)
            self.entry.delete(0, tk.END)
            self.update_canvas()

    def traverse_in_order(self):
        elements = self.binary_tree.traverse_in_order()
        messagebox.showinfo("Traverse", f"Binary Tree In-Order: {elements}")

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_huffman_tree(self, text):
        frequency = Counter(text)
        priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)

        self.root = priority_queue[0]
        self.generate_codes(self.root, "")

    def generate_codes(self, node, current_code):
        if node:
            if node.char is not None:
                self.codes[node.char] = current_code
            self.generate_codes(node.left, current_code + "0")
            self.generate_codes(node.right, current_code + "1")

    def get_encoded_text(self, text):
        return ''.join(self.codes[char] for char in text)


class HuffmanCodingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Huffman Coding")
        self.master.configure(bg="lightgreen")

        self.huffman_coding = HuffmanCoding()

        # Input field for text
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=5)

        # Button to encode text
        self.encode_button = tk.Button(master, text="Encode", command=self.encode_text, bg="lightblue")
        self.encode_button.pack(pady=5)

        # Canvas for tree visualization
        self.canvas = tk.Canvas(master, width=500, height=400, bg="white")
        self.canvas.pack()

    def encode_text(self):
        text = self.text_entry.get()
        if text:
            self.huffman_coding.build_huffman_tree(text)
            encoded_text = self.huffman_coding.get_encoded_text(text)
            messagebox.showinfo("Encoded Text", f"Encoded: {encoded_text}")
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        self.draw_tree(self.huffman_coding.root, 250, 20, 100)

    def draw_tree(self, node, x, y, offset):
        if node:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightgray")
            self.canvas.create_text(x, y, text=node.char if node.char else "*", font=("Arial", 12))
            if node.left:
                self.canvas.create_line(x, y, x - offset, y + 50)
                self.draw_tree(node.left, x - offset, y + 50, offset // 2)
            if node.right:
                self.canvas.create_line(x, y, x + offset, y + 50)
                self.draw_tree(node.right, x + offset, y + 50, offset // 2)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    self.vertices[v].remove(vertex)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
            if vertex1 in self.vertices[vertex2]:
                self.vertices[vertex2].remove(vertex1)

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph")
        self.master.configure(bg="lightblue")

        self.graph = Graph()

        # Input fields
        self.vertex_entry = tk.Entry(master)
        self.vertex_entry.pack(pady=5)

        self.add_vertex_button = tk.Button(master, text="Add Vertex", command=self.add_vertex, bg="lightgreen")
        self.add_vertex_button.pack(pady=5)

        self.remove_vertex_button = tk.Button(master, text="Remove Vertex", command=self.remove_vertex, bg="salmon")
        self.remove_vertex_button.pack(pady=5)

        self.edge_entry1 = tk.Entry(master)
        self.edge_entry1.pack(pady=5)
        self.edge_entry2 = tk.Entry(master)
        self.edge_entry2.pack(pady=5)

        self.add_edge_button = tk.Button(master, text="Add Edge", command=self.add_edge, bg="lightyellow")
        self.add_edge_button.pack(pady=5)

        self.remove_edge_button = tk.Button(master, text="Remove Edge", command=self.remove_edge, bg="lightpink")
        self.remove_edge_button.pack(pady=5)

        # Canvas for graph visualization
        self.canvas = tk.Canvas(master, width=500, height=400, bg="white")
        self.canvas.pack()

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
            self.update_canvas()

    def remove_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.remove_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
            self.update_canvas()

    def add_edge(self):
        vertex1 = self.edge_entry1.get()
        vertex2 = self.edge_entry2.get()
        if vertex1 and vertex2:
            self.graph.add_edge(vertex1, vertex2)
            self.edge_entry1.delete(0, tk.END)
            self.edge_entry2.delete(0, tk.END)
            self.update_canvas()

    def remove_edge(self):
        vertex1 = self.edge_entry1.get()
        vertex2 = self.edge_entry2.get()
        if vertex1 and vertex2:
            self.graph.remove_edge(vertex1, vertex2)
            self.edge_entry1.delete(0, tk.END)
            self.edge_entry2.delete(0, tk.END)
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for i, vertex in enumerate(self.graph.vertices):
            x = 50 + i * 100
            y = 200
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightgray")
            self.canvas.create_text(x, y, text=vertex)
            for neighbor in self.graph.vertices[vertex]:
                neighbor_index = list(self.graph.vertices.keys()).index(neighbor)
                neighbor_x = 50 + neighbor_index * 100
                neighbor_y = 200
                self.canvas.create_line(x, y, neighbor_x, neighbor_y)

class DepthFirstSearch:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def dfs(self, vertex):
        if vertex not in self.visited:
            print(vertex)
            self.visited.add(vertex)
            for neighbor in self.graph.vertices[vertex]:
                self.dfs(neighbor)


class DepthFirstSearchGUI:
    def __init__(self, master, graph):
        self.master = master
        self.master.title("Depth First Search")
        self.master.configure(bg="lightyellow")

        self.graph = graph
        self.dfs = DepthFirstSearch(self.graph)

        self.start_vertex_entry = tk.Entry(master)
        self.start_vertex_entry.pack(pady=5)

        self.start_button = tk.Button(master, text="Start DFS", command=self.start_dfs, bg="lightgreen")
        self.start_button.pack(pady=5)

    def start_dfs(self):
        start_vertex = self.start_vertex_entry.get()
        if start_vertex in self.graph.vertices:
            self.dfs.visited.clear()  # Clear previous visits
            print("DFS Traversal:")
            self.dfs.dfs(start_vertex)
        else:
            print("Vertex not found in graph.")


# Main Application updated to include DFS GUI
class DataStructuresApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Structures Application")
        self.master.geometry("600x600")
        self.graph = {} 

class TravelingSalesman:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.shortest_path = None
        self.min_distance = float('inf')

    def calculate_distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def find_shortest_path(self):
        for perm in itertools.permutations(range(self.num_cities)):
            current_distance = 0
            for i in range(len(perm)):
                current_distance += self.calculate_distance(self.cities[perm[i]], self.cities[perm[(i + 1) % self.num_cities]])
            if current_distance < self.min_distance:
                self.min_distance = current_distance
                self.shortest_path = perm

class TravelingSalesmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Traveling Salesman Problem")
        self.master.configure(bg="lightgreen")

        self.cities = []
        self.tsp = TravelingSalesman(self.cities)

        self.canvas = tk.Canvas(master, width=500, height=400, bg="white")
        self.canvas.pack()

        self.add_city_button = tk.Button(master, text="Add City", command=self.add_city, bg="lightblue")
        self.add_city_button.pack(pady=5)

        self.solve_button = tk.Button(master, text="Solve TSP", command=self.solve_tsp, bg="lightcoral")
        self.solve_button.pack(pady=5)

    def add_city(self):
        # For demonstration, we add cities at random positions
        x = random.randint(20, 480)
        y = random.randint(20, 380)
        self.cities.append((x, y))
        self.update_canvas()

    def solve_tsp(self):
        self.tsp = TravelingSalesman(self.cities)
        self.tsp.find_shortest_path()
        if self.tsp.shortest_path:
            path = " -> ".join(str(self.tsp.shortest_path[i]) for i in range(len(self.tsp.shortest_path)))
            messagebox.showinfo("Shortest Path", f"Path: {path}\nDistance: {self.tsp.min_distance:.2f}")
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for i, city in enumerate(self.cities):
            x, y = city
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")
            self.canvas.create_text(x, y, text=f"City {i + 1}", font=("Arial", 10))

        # Draw the path if exists
        if self.tsp.shortest_path:
            for i in range(len(self.tsp.shortest_path)):
                start = self.cities[self.tsp.shortest_path[i]]
                end = self.cities[self.tsp.shortest_path[(i + 1) % len(self.tsp.shortest_path)]]
                self.canvas.create_line(start[0], start[1], end[0], end[1], fill="red")
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index] = key

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] == key:
            self.table[index] = None

    def traverse(self):
        return [key for key in self.table if key is not None]

class HashTableGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Hash Table")
        self.master.configure(bg="lightblue")

        self.hash_table = HashTable()

        self.key_entry = tk.Entry(master)
        self.key_entry.pack(pady=5)

        self.insert_button = tk.Button(master, text="Insert", command=self.insert_key, bg="lightgreen")
        self.insert_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_key, bg="salmon")
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_table, bg="lightyellow")
        self.traverse_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", bg="lightblue")
        self.result_label.pack(pady=5)

    def insert_key(self):
        key = int(self.key_entry.get())
        self.hash_table.insert(key)
        self.key_entry.delete(0, tk.END)

    def delete_key(self):
        key = int(self.key_entry.get())
        self.hash_table.delete(key)
        self.key_entry.delete(0, tk.END)

    def traverse_table(self):
        keys = self.hash_table.traverse()
        self.result_label.config(text=f"Table: {keys}")

class ChainedHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def traverse(self):
        return [(i, bucket) for i, bucket in enumerate(self.table) if bucket]

class ChainedHashTableGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chained Hash Table")
        self.master.configure(bg="lightyellow")

        self.hash_table = ChainedHashTable()

        self.key_entry = tk.Entry(master)
        self.key_entry.pack(pady=5)

        self.insert_button = tk.Button(master, text="Insert", command=self.insert_key, bg="lightgreen")
        self.insert_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_key, bg="salmon")
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse_table, bg="lightblue")
        self.traverse_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", bg="lightyellow")
        self.result_label.pack(pady=5)

    def insert_key(self):
        key = int(self.key_entry.get())
        self.hash_table.insert(key)
        self.key_entry.delete(0, tk.END)

    def delete_key(self):
        key = int(self.key_entry.get())
        self.hash_table.delete(key)
        self.key_entry.delete(0, tk.END)

    def traverse_table(self):
        buckets = self.hash_table.traverse()
        self.result_label.config(text=f"Table: {buckets}")

class DataStructuresApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Structures Application")
        self.master.geometry("600x600")
        self.graph = Graph()

        # Buttons to open each data structure GUI
        self.stack_button = tk.Button(master, text="Stack", command=self.open_stack, bg="lightblue", width=15)
        self.stack_button.pack(pady=5)

        self.queue_button = tk.Button(master, text="Queue", command=self.open_queue, bg="lightgreen", width=15)
        self.queue_button.pack(pady=5)

        self.dll_button = tk.Button(master, text="Doubly Linked List", command=self.open_dll, bg="lightpink", width=15)
        self.dll_button.pack(pady=5)

        self.priority_queue_button = tk.Button(master, text="Priority Queue", command=self.open_priority_queue, bg="lightcyan", width=15)
        self.priority_queue_button.pack(pady=5)

        self.binary_tree_button = tk.Button(master, text="Binary Tree", command=self.open_binary_tree, bg="lightyellow", width=15)
        self.binary_tree_button.pack(pady=5)

        self.huffman_coding_button = tk.Button(master, text="Huffman Coding", command=self.open_huffman_coding, bg="lightcoral", width=15)
        self.huffman_coding_button.pack(pady=5)

        self.graph_button = tk.Button(master, text="Graph", command=self.open_graph, bg="lightcoral", width=15)
        self.graph_button.pack(pady=5)

        self.tsp_button = tk.Button(master, text="TSP", command=self.open_tsp, bg="lightblue", width=15)
        self.tsp_button.pack(pady=5)

        self.hash_table_button = tk.Button(master, text="Basic Hash Table", command=self.open_hash_table, bg="lightcoral", width=15)
        self.hash_table_button.pack(pady=5)

        self.chained_hash_table_button = tk.Button(master, text="Chained Hash Table", command=self.open_chained_hash_table, bg="lightcoral", width=15)
        self.chained_hash_table_button.pack(pady=5)

        self.dfs_button = tk.Button(master, text="Depth First Search", command=self.open_dfs, bg="lightcoral", width=15)
        self.dfs_button.pack(pady=5)

    def open_dfs(self):
        dfs_window = tk.Toplevel(self.master)
        DepthFirstSearchGUI(dfs_window, self.graph)

    def open_chained_hash_table(self):
        chained_hash_table_window = tk.Toplevel(self.master)
        ChainedHashTableGUI(chained_hash_table_window)

    def open_hash_table(self):
        hash_table_window = tk.Toplevel(self.master)
        HashTableGUI(hash_table_window)

    def open_tsp(self):
        tsp_window = tk.Toplevel(self.master)
        TravelingSalesmanGUI(tsp_window)

    def open_dfs(self):
        dfs_window = tk.Toplevel(self.master)
        DepthFirstSearchGUI(dfs_window, self.graph)

    def open_graph(self):
        graph_window = tk.Toplevel(self.master)
        GraphGUI(graph_window)

    def open_huffman_coding(self):
        huffman_window = tk.Toplevel(self.master)
        HuffmanCodingGUI(huffman_window)


    def open_stack(self):
        stack_window = tk.Toplevel(self.master)
        StackGUI(stack_window)

    def open_queue(self):
        queue_window = tk.Toplevel(self.master)
        QueueGUI(queue_window)

    def open_dll(self):
        dll_window = tk.Toplevel(self.master)
        DoublyLinkedListGUI(dll_window)

    def open_priority_queue(self):
        pq_window = tk.Toplevel(self.master)
        PriorityQueueGUI(pq_window)

    def open_binary_tree(self):
        bt_window = tk.Toplevel(self.master)
        BinaryTreeGUI(bt_window)


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = DataStructuresApp(root)
    root.mainloop()
