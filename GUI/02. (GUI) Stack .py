import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Operations")
        self.stack = Stack()
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="#D0E8F2")

        self.title_label = tk.Label(self.root, text="Stack Operations", font=("Helvetica", 20, "bold"), bg="#083D77", fg="#FFFFFF")
        self.title_label.pack(pady=20)

        self.entry_frame = tk.Frame(self.root, bg="#D0E8F2")
        self.entry_frame.pack(pady=10)
        
        self.entry_label = tk.Label(self.entry_frame, text="Enter Element:", font=("Helvetica", 14), bg="#D0E8F2", fg="#000000")
        self.entry_label.pack(side=tk.LEFT, padx=5)
        
        self.entry = tk.Entry(self.entry_frame, width=25, font=("Helvetica", 14))
        self.entry.pack(side=tk.LEFT, padx=5)

        self.button_frame = tk.Frame(self.root, bg="#A3CEF1")
        self.button_frame.pack(pady=20)

        self.button_style = {"width": 20, "font": ("Helvetica", 12), "bg": "#1B4F72", "fg": "#FFFFFF", "bd": 0, "relief": "flat"}

        self.insert_button = tk.Button(self.button_frame, text="Insert (Push)", command=self.insert_element, **self.button_style)
        self.insert_button.grid(row=0, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete (Pop)", command=self.delete_element, **self.button_style)
        self.delete_button.grid(row=0, column=1, padx=10, pady=5)

        self.peek_button = tk.Button(self.button_frame, text="Peek", command=self.peek_element, **self.button_style)
        self.peek_button.grid(row=1, column=0, padx=10, pady=5)

        self.empty_button = tk.Button(self.button_frame, text="Is Empty", command=self.check_if_empty, **self.button_style)
        self.empty_button.grid(row=1, column=1, padx=10, pady=5)

        self.size_button = tk.Button(self.button_frame, text="Get Size", command=self.get_size, **self.button_style)
        self.size_button.grid(row=2, column=0, padx=10, pady=5)

        self.traverse_button = tk.Button(self.button_frame, text="Traversal (Display Stack)", command=self.traverse_stack, **self.button_style)
        self.traverse_button.grid(row=2, column=1, padx=10, pady=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.root.quit, **self.button_style)
        self.quit_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.result_display = tk.Text(self.root, height=12, width=50, state=tk.DISABLED, font=("Helvetica", 12), bg="#F1F3F8", fg="#000000", wrap=tk.WORD)
        self.result_display.pack(pady=10)

    def insert_element(self):
        element = self.entry.get()
        if element:
            self.stack.push(element)
            self.entry.delete(0, tk.END)
            self.update_display()
        else:
            messagebox.showwarning("Warning", "Please enter an element.")

    def delete_element(self):
        try:
            popped_item = self.stack.pop()
            messagebox.showinfo("Deleted Item", f"Deleted item: {popped_item}")
            self.update_display()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_element(self):
        try:
            top_item = self.stack.peek()
            messagebox.showinfo("Top Item", f"Top item: {top_item}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def check_if_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Check if Empty", "The stack is empty.")
        else:
            messagebox.showinfo("Check if Empty", "The stack is not empty.")

    def get_size(self):
        size = self.stack.size()
        messagebox.showinfo("Get Size", f"Size of stack: {size}")

    def traverse_stack(self):
        self.update_display()

    def update_display(self):
        self.result_display.config(state=tk.NORMAL)
        self.result_display.delete(1.0, tk.END)
        self.result_display.insert(tk.END, str(self.stack))
        self.result_display.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.geometry("600x500")
    app = StackGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
