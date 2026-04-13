class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, items):
        self.queue.extend(items)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def traversal(self):
        return self.queue.copy()

def main():
    queue = Queue()

    while True:
        print("\n1. Enqueue items")
        print("2. Dequeue item")
        print("3. Traversal")
        print("4. Size")
        print("5. Is Empty")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            items = input("Enter items to enqueue (separated by space): ").split()
            queue.enqueue(items)
            print("Items enqueued successfully")
        elif choice == "2":
            item = queue.dequeue()
            if item:
                print("Dequeued item:", item)
            else:
                print("Queue is empty")
        elif choice == "3":
            items = queue.traversal()
            if items:
                print("Queue traversal:", ", ".join(items))
            else:
                print("Queue is empty")
        elif choice == "4":
            print("Queue size:", queue.size())
        elif choice == "5":
            if queue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
