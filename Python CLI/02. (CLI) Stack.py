class Stack:
  
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if self.is_empty():
      return None
    return self.items.pop()

  def peek(self):
    if self.is_empty():
      return None
    return self.items[-1]

  def size(self):
    return len(self.items)

  def print_stack(self):
    print("Stack elements:")
    for item in self.items[::-1]:
      print(item)


# Create a stack
stack = Stack()

# Test stack operations
stack.push(10)
stack.push(20)
stack.push(30)
print("Peek element: ",stack.peek())

print("Stack size:", stack.size())
print("Popped element:", stack.pop())

stack.print_stack()
