class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Queue: " + str(self.items)


# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Output: Queue: [1, 2, 3]
    print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
    print("Peek:", queue.peek())  # Output: Peek: 2
    print(queue)  # Output: Queue: [2, 3]
    print("Size:", queue.size())  # Output: Size: 2
