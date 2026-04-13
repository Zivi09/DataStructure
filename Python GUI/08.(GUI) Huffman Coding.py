import customtkinter as ctk
from tkinter import messagebox
import heapq
from collections import defaultdict

# Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman tree

# Function to generate Huffman codes from the tree
def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to calculate the frequency of each character in the text
def calculate_frequency(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

# Function to encode the text using the generated Huffman codes
def huffman_encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

# Function to decode the encoded text using the Huffman tree
def huffman_decode(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# Function to draw the Huffman Tree on a Canvas
def draw_huffman_tree(node, canvas, x, y, x_offset, y_offset):
    if node is not None:
        # Draw the circle for the node
        radius = 20
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")

        # Draw the character or frequency in the circle
        if node.char is not None:
            text = f"{node.char}"
        else:
            text = f"{node.freq}"
        
        canvas.create_text(x, y, text=text)

        if node.left:
            # Draw line to left child and recursively draw the left subtree
            canvas.create_line(x, y + radius, x - x_offset, y + y_offset - radius)
            draw_huffman_tree(node.left, canvas, x - x_offset, y + y_offset, x_offset // 2, y_offset)

        if node.right:
            # Draw line to right child and recursively draw the right subtree
            canvas.create_line(x, y + radius, x + x_offset, y + y_offset - radius)
            draw_huffman_tree(node.right, canvas, x + x_offset, y + y_offset, x_offset // 2, y_offset)

# Function to handle Huffman Coding process and update GUI
def huffman_coding():
    text = input_text.get("1.0", ctk.END).strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to encode.")
        return

    frequency = calculate_frequency(text)
    root = build_huffman_tree(frequency)
    codes = generate_huffman_codes(root)

    encoded_text = huffman_encode(text, codes)
    decoded_text = huffman_decode(encoded_text, root)

    original_size = len(text) * 8  # 8 bits per character in ASCII
    compressed_size = len(encoded_text)  # size in bits

    codes_text.set(f"Huffman Codes: {codes}")
    encoded_text_display.set(f"Encoded Text: {encoded_text}")
    decoded_text_display.set(f"Decoded Text: {decoded_text}")
    size_comparison.set(f"Original Size: {original_size} bits\nCompressed Size: {compressed_size} bits")

    canvas.delete("all")  # Clear the canvas before drawing the tree
    draw_huffman_tree(root, canvas, 300, 20, 150, 60)

# Setting up the GUI
root = ctk.CTk()
root.title("Huffman Coding GUI")
root.geometry("600x750")

# Input text label and field
ctk.CTkLabel(root, text="Enter text to encode:").pack(pady=5)
input_text = ctk.CTkTextbox(root, wrap=ctk.WORD, width=400, height=50)
input_text.pack(pady=5)

# Button to trigger Huffman Coding
ctk.CTkButton(root, text="Encode and Decode", command=huffman_coding).pack(pady=10)

# Output labels
codes_text = ctk.StringVar()
encoded_text_display = ctk.StringVar()
decoded_text_display = ctk.StringVar()
size_comparison = ctk.StringVar()

ctk.CTkLabel(root, textvariable=codes_text).pack(pady=5)
ctk.CTkLabel(root, textvariable=encoded_text_display).pack(pady=5)
ctk.CTkLabel(root, textvariable=decoded_text_display).pack(pady=5)
ctk.CTkLabel(root, textvariable=size_comparison).pack(pady=10)

# Canvas to draw the Huffman Tree
canvas = ctk.CTkCanvas(root, width=800, height=600, bg="white")
canvas.pack(pady=10)

# Run the GUI main loop
root.mainloop()