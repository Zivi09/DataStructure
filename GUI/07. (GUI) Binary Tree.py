import customtkinter as ctk
from tkinter import messagebox

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.value < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)

    def preorder_traversal(self, root, result):
        if root:
            result.append(root.value)
            self.preorder_traversal(root.left, result)
            self.preorder_traversal(root.right, result)

    def postorder_traversal(self, root, result):
        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.value)

class BinaryTreeApp:
    def __init__(self, root):
        self.tree = BinaryTree()
        self.root = root
        self.root.title("Binary Tree Operations")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label = ctk.CTkLabel(root, text="Binary Tree Operations", font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.insert_frame = ctk.CTkFrame(root)
        self.insert_frame.pack(pady=10)
        self.insert_label = ctk.CTkLabel(self.insert_frame, text="Insert Value:")
        self.insert_label.pack(side=ctk.LEFT)
        self.insert_entry = ctk.CTkEntry(self.insert_frame)
        self.insert_entry.pack(side=ctk.LEFT, padx=5)
        self.insert_button = ctk.CTkButton(self.insert_frame, text="Insert", command=self.insert_value)
        self.insert_button.pack(side=ctk.LEFT, padx=5)

        self.delete_frame = ctk.CTkFrame(root)
        self.delete_frame.pack(pady=10)
        self.delete_label = ctk.CTkLabel(self.delete_frame, text="Delete Value:")
        self.delete_label.pack(side=ctk.LEFT)
        self.delete_entry = ctk.CTkEntry(self.delete_frame)
        self.delete_entry.pack(side=ctk.LEFT, padx=5)
        self.delete_button = ctk.CTkButton(self.delete_frame, text="Delete", command=self.delete_value)
        self.delete_button.pack(side=ctk.LEFT, padx=5)

        self.traversal_frame = ctk.CTkFrame(root)
        self.traversal_frame.pack(pady=10)
        self.inorder_button = ctk.CTkButton(self.traversal_frame, text="In-order Traversal", command=self.inorder_traversal)
        self.inorder_button.pack(side=ctk.LEFT, padx=5)
        self.preorder_button = ctk.CTkButton(self.traversal_frame, text="Pre-order Traversal", command=self.preorder_traversal)
        self.preorder_button.pack(side=ctk.LEFT, padx=5)
        self.postorder_button = ctk.CTkButton(self.traversal_frame, text="Post-order Traversal", command=self.postorder_traversal)
        self.postorder_button.pack(side=ctk.LEFT, padx=5)

        # Labels for displaying traversal results
        self.inorder_label = ctk.CTkLabel(root, text="In-order Traversal: ", font=('Helvetica', 14))
        self.inorder_label.pack(pady=5)
        self.preorder_label = ctk.CTkLabel(root, text="Pre-order Traversal: ", font=('Helvetica', 14))
        self.preorder_label.pack(pady=5)
        self.postorder_label = ctk.CTkLabel(root, text="Post-order Traversal: ", font=('Helvetica', 14))
        self.postorder_label.pack(pady=5)

        self.canvas = ctk.CTkCanvas(root, width=800, height=400, bg="white")
        self.canvas.pack(pady=10)

    def insert_value(self):
        value = self.insert_entry.get()
        if value.isdigit():
            self.tree.root = self.tree.insert(self.tree.root, int(value))
            self.insert_entry.delete(0, ctk.END)
            messagebox.showinfo("Success", f"Inserted {value} into the tree.")
            self.draw_tree()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def delete_value(self):
        value = self.delete_entry.get()
        if value.isdigit():
            self.tree.root = self.tree.delete(self.tree.root, int(value))
            self.delete_entry.delete(0, ctk.END)
            messagebox.showinfo("Success", f"Deleted {value} from the tree.")
            self.draw_tree()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def inorder_traversal(self):
        result = []
        self.tree.inorder_traversal(self.tree.root, result)
        self.inorder_label.configure(text="In-order Traversal: " + " ".join(map(str, result)))

    def preorder_traversal(self):
        result = []
        self.tree.preorder_traversal(self.tree.root, result)
        self.preorder_label.configure(text="Pre-order Traversal: " + " ".join(map(str, result)))

    def postorder_traversal(self):
        result = []
        self.tree.postorder_traversal(self.tree.root, result)
        self.postorder_label.configure(text="Post-order Traversal: " + " ".join(map(str, result)))

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_node(self.tree.root, 400, 20, 200)

    def _draw_node(self, node, x, y, x_offset):
        if node:
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.value), font=('Helvetica', 12, 'bold'))

            if node.left:
                self.canvas.create_line(x, y + 20, x - x_offset, y + 80)
                self._draw_node(node.left, x - x_offset, y + 80, x_offset // 2)

            if node.right:
                self.canvas.create_line(x, y + 20, x + x_offset, y + 80)
                self._draw_node(node.right, x + x_offset, y + 80, x_offset // 2)

if __name__ == "__main__":
    root = ctk.CTk()
    app = BinaryTreeApp(root)
    root.mainloop()
