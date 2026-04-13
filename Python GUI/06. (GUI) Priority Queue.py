import tkinter as tk
from tkinter import messagebox
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def delete(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

    def traversal(self):
        return [item for _, item in self.queue]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.queue = PriorityQueue()

    def create_widgets(self):
        self.insert_frame = tk.Frame(self)
        self.insert_frame.pack(side="top", pady=10)

        self.insert_label = tk.Label(self.insert_frame, text="Enter item and priority to insert:", font=("Arial", 14))
        self.insert_label.pack(side="left", padx=10)

        self.insert_entry_item = tk.Entry(self.insert_frame, font=("Arial", 14), width=10, highlightthickness=1)
        self.insert_entry_item.pack(side="left", padx=10)

        self.insert_entry_priority = tk.Entry(self.insert_frame, font=("Arial", 14), width=10, highlightthickness=1)
        self.insert_entry_priority.pack(side="left", padx=10)

        self.insert_button = tk.Button(self.insert_frame, text="Enqueue", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.insert_button.pack(side="left", padx=10)
        self.insert_button.config(command=self.insert_item)

##        self.insert_frame = tk.Frame(self)
##        self.insert_frame.pack(side="top", pady=10)
##
##        self.insert_label = tk.Label(self.insert_frame, text="Enter item and priority to insert:", font=("Arial", 14))
##        self.insert_label.pack(side="left", padx=10)
##
##        self.insert_entry_item = tk.Entry(self.insert_frame, font=("Arial", 14), width=20)
##        self.insert_entry_item.pack(side="left", padx=10)
##
##        self.insert_entry_priority = tk.Entry(self.insert_frame, font=("Arial", 14), width=10)
##        self.insert_entry_priority.pack(side="left", padx=10)
##
##        self.insert_button = tk.Button(self.insert_frame, text="Insert", font=("Arial", 14), width=10, height=1)
##        self.insert_button.pack(side="left", padx=10)
##        self.insert_button.config(command=self.insert_item)

        self.delete_frame = tk.Frame(self)
        self.delete_frame.pack(side="top", pady=10)

        self.delete_button  = tk.Button(self.delete_frame, text="Dequeue", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.delete_button.pack(side="left", padx=10)
        self.delete_button.config(command=self.delete_item)

##        self.delete_frame = tk.Frame(self)
##        self.delete_frame.pack(side="top", pady=10)
##
##        self.delete_button = tk.Button(self.delete_frame, text="Delete", font=("Arial", 14), width=10, height=1)
##        self.delete_button.pack(side="left", padx=10)
##        self.delete_button.config(command=self.delete_item)

        self.traversal_frame = tk.Frame(self)
        self.traversal_frame.pack(side="top", pady=10)

        self.traversal_button = tk.Button(self.traversal_frame, text="Traversal", font=("Arial", 14), width=10, height=1, relief="ridge", bd=5)
        self.traversal_button.pack(side="left", padx=10)
        self.traversal_button.config(command=self.traversal)
##        self.traversal_frame = tk.Frame(self)
##        self.traversal_frame.pack(side="top", pady=10)
##
##        self.traversal_button = tk.Button(self.traversal_frame, text="Traversal", font=("Arial", 14), width=10, height=1)
##        self.traversal_button.pack(side="left", padx=10)
##        self.traversal_button.config(command=self.traversal)

    def insert_item(self):
        item = self.insert_entry_item.get()
        priority = self.insert_entry_priority.get()
        if item and priority:
            try:
                priority = int(priority)
                self.queue.insert(item, priority)
                self.insert_entry_item.delete(0, "end")
                self.insert_entry_priority.delete(0, "end")
            except ValueError:
                messagebox.showerror("Error", "Priority must be an integer")
        else:
            messagebox.showerror("Error", "Please enter an item and priority")

    def delete_item(self):
        item = self.queue.delete()
        if item:
            messagebox.showinfo("Deleted item", item)
        else:
            messagebox.showerror("Error", "Priority queue is empty")

    def traversal(self):
        items = self.queue.traversal()
        messagebox.showinfo("Priority queue traversal", ", ".join(items))

root = tk.Tk()
root.title("Priority Queue Operations")
root.geometry("700x300")
app = Application(master=root)
app.mainloop()
