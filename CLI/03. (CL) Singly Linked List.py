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
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")


# Create a linked list
linked_list = LinkedList()

# Insert elements
linked_list.insert_at_beginning(50)
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(10)

# Print the linked list
print("Linked list:")
linked_list.traverse()

# Delete elements from beginning and end
deleted_data = linked_list.delete_at_beginning()
if deleted_data:
  print("Deleted from beginning:", deleted_data)
deleted_data = linked_list.delete_at_end()
if deleted_data:
  print("Deleted from end:", deleted_data)

# Print the linked list after deletions
print("Linked list after deletions:")
linked_list.traverse()
