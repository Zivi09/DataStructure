import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        return deleted_node.data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

class GUI:
    def __init__(self, master):
        self.master = master
        self.linked_list = LinkedList()
        root.geometry("400x400")

        self.insert_at_beginning_label = tk.Label(master, text="Insert at beginning:")
        self.insert_at_beginning_label.pack()

        self.insert_at_beginning_entry = tk.Entry(master)
        self.insert_at_beginning_entry.pack()

        self.insert_at_beginning_button = tk.Button(master, text="Insert", command=self.insert_at_beginning)
        self.insert_at_beginning_button.pack()

        self.insert_at_end_label = tk.Label(master, text="Insert at end:")
        self.insert_at_end_label.pack()

        self.insert_at_end_entry = tk.Entry(master)
        self.insert_at_end_entry.pack()

        self.insert_at_end_button = tk.Button(master, text="Insert", command=self.insert_at_end)
        self.insert_at_end_button.pack()

        self.delete_at_beginning_button = tk.Button(master, text="Delete at beginning", command=self.delete_at_beginning)
        self.delete_at_beginning_button.pack()

        self.delete_at_end_button = tk.Button(master, text="Delete at end", command=self.delete_at_end)
        self.delete_at_end_button.pack()

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse)
        self.traverse_button.pack()

    def insert_at_beginning(self):
        data = self.insert_at_beginning_entry.get()
        if data:
            self.linked_list.insert_at_beginning(int(data))
            self.insert_at_beginning_entry.delete(0, tk.END)

    def insert_at_end(self):
        data = self.insert_at_end_entry.get()
        if data:
            self.linked_list.insert_at_end(int(data))
            self.insert_at_end_entry.delete(0, tk.END)

    def delete_at_beginning(self):
        deleted_data = self.linked_list.delete_at_beginning()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", "Deleted from beginning: " + str(deleted_data))

    def delete_at_end(self):
        deleted_data = self.linked_list.delete_at_end()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", "Deleted from end: " + str(deleted_data))

    def traverse(self):
        elements = self.linked_list.traverse()
        messagebox.showinfo("Linked List", elements)

root = tk.Tk()
my_gui = GUI(root)
root.mainloop()

