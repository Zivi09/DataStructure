import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _ascii_hash_function(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, key):
        index = self._ascii_hash_function(key)
        self.table[index] = key

    def remove(self, key):
        index = self._ascii_hash_function(key)
        if self.table[index] == key:
            self.table[index] = None

    def contains(self, key):
        index = self._ascii_hash_function(key)
        return self.table[index] == key

    def display(self):
        return self.table

    def hash_code(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum, ascii_sum % self.size

class HashTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Table without Collision Handling")
        self.hash_table = HashTable()
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Hash Set", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.display_area = tk.Text(root, height=12, width=50, font=("Arial", 16), bg="#ffffff", borderwidth=2, relief="groove")
        self.display_area.pack(pady=10)

        self.hash_code_label = tk.Label(root, text="Hash Code (ASCII Sum)", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.hash_code_label.pack(pady=10)
        
        self.hash_code_value = tk.Label(root, text="", font=("Arial", 16), fg="blue", bg="#f0f0f0")
        self.hash_code_value.pack(pady=10)

        self.entry = tk.Entry(root, width=30, font=("Arial", 16))
        self.entry.pack(pady=20)

        self.btn_frame = tk.Frame(root, bg="#f0f0f0")
        self.btn_frame.pack(pady=10)

        self.add_btn = tk.Button(self.btn_frame, text="add()", command=self.add, width=10, font=("Arial", 14))
        self.add_btn.grid(row=0, column=0, padx=10)

        self.remove_btn = tk.Button(self.btn_frame, text="remove()", command=self.remove, width=10, font=("Arial", 14))
        self.remove_btn.grid(row=0, column=1, padx=10)

        self.contains_btn = tk.Button(self.btn_frame, text="contains()", command=self.contains, width=10, font=("Arial", 14))
        self.contains_btn.grid(row=1, column=0, padx=10, pady=10)

        self.size_btn = tk.Button(self.btn_frame, text="size()", command=self.size, width=10, font=("Arial", 14))
        self.size_btn.grid(row=1, column=1, padx=10, pady=10)

        self.update_display()

    def update_display(self):
        self.display_area.delete('1.0', tk.END)
        hash_table = self.hash_table.display()
        for i, key in enumerate(hash_table):
            if key is not None:
                self.display_area.insert(tk.END, f"{i} : {key}\n")
            else:
                self.display_area.insert(tk.END, f"{i} :\n")

    def update_hash_code(self, key):
        ascii_sum, hash_code = self.hash_table.hash_code(key)
        self.hash_code_value.config(text=f"Sum of ASCII: {ascii_sum}, Hash Code: {ascii_sum} % {self.hash_table.size} = {hash_code}")

    def add(self):
        key = self.entry.get().strip()
        if key:
            self.hash_table.insert(key)
            self.update_hash_code(key)
            self.update_display()

    def remove(self):
        key = self.entry.get().strip()
        if key:
            self.hash_table.remove(key)
            self.update_hash_code(key)
            self.update_display()

    def contains(self):
        key = self.entry.get().strip()
        if key:
            found = self.hash_table.contains(key)
            if found:
                messagebox.showinfo("Result", f"'{key}' is in the hash table.")
            else:
                messagebox.showinfo("Result", f"'{key}' is not in the hash table.")
            self.update_hash_code(key)

    def size(self):
        size = sum(1 for key in self.hash_table.display() if key is not None)
        messagebox.showinfo("Size", f"Hash table contains {size} elements.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
