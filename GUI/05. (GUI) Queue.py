import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.queue = Queue()

    def create_widgets(self):
        self.enqueue_frame = tk.Frame(self)
        self.enqueue_frame.pack(side="top", pady=10)

        self.enqueue_label = tk.Label(self.enqueue_frame, text="Enter item to enqueue:", font=("Arial", 14))
        self.enqueue_label.pack(side="left", padx=10)

        self.enqueue_entry = tk.Entry(self.enqueue_frame, font=("Arial", 14), width=20, highlightthickness=1)
        self.enqueue_entry.pack(side="left", padx=10)

        self.enqueue_button = tk.Button(self.enqueue_frame, text="Enqueue", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.enqueue_button.pack(side="left", padx=10)
        self.enqueue_button.config(command=self.enqueue_item)

        self.dequeue_frame = tk.Frame(self)
        self.dequeue_frame.pack(side="top", pady=10)

        self.dequeue_button = tk.Button(self.dequeue_frame, text="Dequeue", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.dequeue_button.pack(side="left", padx=10)
        self.dequeue_button.config(command=self.dequeue_item)

        self.traversal_frame = tk.Frame(self)
        self.traversal_frame.pack(side="top", pady=10)

        self.traversal_button = tk.Button(self.traversal_frame, text="Traversal", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.traversal_button.pack(side="left", padx=10)
        self.traversal_button.config(command=self.traversal)

        self.size_frame = tk.Frame(self)
        self.size_frame.pack(side="top", pady=10)

        self.size_button = tk.Button(self.size_frame, text="Size", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.size_button.pack(side="left", padx=10)
        self.size_button.config(command=self.size)

        self.is_empty_frame = tk.Frame(self)
        self.is_empty_frame.pack(side="top", pady=10)

        self.is_empty_button = tk.Button(self.is_empty_frame, text="Is Empty", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.is_empty_button.pack(side="left", padx=10)
        self.is_empty_button.config(command=self.is_empty)

    def enqueue_item(self):
        item = self.enqueue_entry.get()
        if item:
            self.queue.enqueue(item)
            self.enqueue_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter an item to enqueue")

    def dequeue_item(self):
        item = self.queue.dequeue()
        if item:
            messagebox.showinfo("Dequeued item", item)
        else:
            messagebox.showerror("Error", "Queue is empty")

    def traversal(self):
        items = self.queue.queue.copy()
        messagebox.showinfo("Queue traversal", ", ".join(items))

    def size(self):
        messagebox.showinfo("Queue size", str(self.queue.size()))

    def is_empty(self):
        if self.queue.is_empty():
            messagebox.showinfo("Is empty", "Yes")
        else:
            messagebox.showinfo("Is empty", "No")

root = tk.Tk()
root.title("Queue Operations")
root.geometry("700x300")
app = Application(master=root)
app.mainloop()
