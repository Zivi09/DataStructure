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
    while current:
      print(current.data, end=" <-> ")
      current = current.next
    print("None")

if __name__ == '__main__':
  # Create a doubly linked list
  linked_list = DoublyLinkedList()

  print("~~~~~~~~ DoublyLinkedList ~~~~~~~~~")

  # Insert elements
  ele = int(input("Enter element to insert at the beginning : "))
  linked_list.insert_at_beginning(ele)
  ele = int(input("Enter element to insert at the end : "))
  linked_list.insert_at_end(ele)
  ele = int(input("Enter element to insert at the beginning : "))
  linked_list.insert_at_beginning(ele)
  ele = int(input("Enter element to insert at the end : "))
  linked_list.insert_at_end(ele)

  # Print the linked list
  print("Doubly Linked List:")
  linked_list.traverse()

  # Delete elements from beginning and end
  deleted_data = linked_list.delete_at_beginning()
  if deleted_data:
    print("Deleted from beginning:", deleted_data)
  deleted_data = linked_list.delete_at_end()
  if deleted_data:
    print("Deleted from end:", deleted_data)

  # Print the linked list after deletions
  print("Doubly Linked List after deletions:")
  linked_list.traverse()
