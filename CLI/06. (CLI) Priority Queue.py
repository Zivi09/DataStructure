import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, items, priorities):
        for item, priority in zip(items, priorities):
            heapq.heappush(self.queue, (priority, item))

    def size(self):
        return len(self.queue)        

    def dequeue(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

    def traversal(self):
        return [item for _, item in self.queue]

def main():
    queue = PriorityQueue()

    while True:
        print("\n1. Enqueue items")
        print("2. Dequeue item")
        print("3. Traversal")
        print("4. Size")
        print("5. Is Empty")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            items = input("Enter items (separated by space): ").split()
            priorities = list(map(int, input("Enter priorities (separated by space): ").split()))
            queue.insert(items, priorities)
            print("Items enqueued successfully")
        elif choice == "2":
            item = queue.dequeue()
            if item:
                print("Dequeue item:", item)
            else:
                print("Priority queue is empty")
        elif choice == "3":
            items = queue.traversal()
            if items:
                print("Priority queue traversal:", ", ".join(items))
            else:
                print("Priority queue is empty")
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
