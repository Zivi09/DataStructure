import tkinter as tk
from tkinter import messagebox

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head is None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.is_empty():
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.is_empty():
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def delete_at_beginning(self):
    if self.is_empty():
      return None
    deleted_node = self.head
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
    return deleted_node.data

  def delete_at_end(self):
    if self.is_empty():
      return None
    deleted_node = self.tail
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    return deleted_node.data

  def traverse(self): 
    current = self.head
    linked_list_str = ""
    while current:
      linked_list_str += str(current.data) + " <-> "
      current = current.next
    linked_list_str += "None"
    return linked_list_str


class GUI:
  def __init__(self, master):
    self.master = master
    self.master.title("Doubly Linked List GUI")
    self.linked_list = DoublyLinkedList()
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

    self.result_label = tk.Label(master, text="")
    self.result_label.pack()

  def insert_at_beginning(self):
    try:
      data = int(self.insert_at_beginning_entry.get())
      self.linked_list.insert_at_beginning(data)
      self.insert_at_beginning_entry.delete(0, tk.END)
      self.result_label.config(text="Inserted at beginning: " + str(data))
    except ValueError:
      messagebox.showerror("Error", "Invalid input. Please enter an integer.")

  def insert_at_end(self):
    try:
      data = int(self.insert_at_end_entry.get())
      self.linked_list.insert_at_end(data)
      self.insert_at_end_entry.delete(0, tk.END)
      self.result_label.config(text="Inserted at end: " + str(data))
    except ValueError:
      messagebox.showerror("Error", "Invalid input. Please enter an integer.")

  def delete_at_beginning(self):
    deleted_data = self.linked_list.delete_at_beginning()
    if deleted_data is not None:
      self.result_label.config(text="Deleted from beginning: " + str(deleted_data))
    else:
      self.result_label.config(text="List is empty.")

  def delete_at_end(self):
    deleted_data = self.linked_list.delete_at_end()
    if deleted_data is not None:
      self.result_label.config(text="Deleted from end: " + str(deleted_data))
    else:
      self.result_label.config(text="List is empty.")

  def traverse(self):
    linked_list_str = self.linked_list.traverse()
    self.result_label.config(text="Doubly Linked List: " + linked_list_str)


root = tk.Tk()
gui = GUI(root)
root.mainloop()
