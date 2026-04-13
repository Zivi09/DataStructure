import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Queue<T> {
    private List<T> queue;

    public Queue() {
        this.queue = new ArrayList<>();
    }

    public void enqueue(T[] items) {
        for (T item : items) {
            queue.add(item);
        }
    }

    public T dequeue() {
        if (queue.size() < 1) {
            return null;
        }
        return queue.remove(0);
    }

    public int size() {
        return queue.size();
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public List<T> traversal() {
        return new ArrayList<>(queue);
    }

    public static void main(String[] args) {
        Queue<String> queue = new Queue<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Enqueue items");
            System.out.println("2. Dequeue item");
            System.out.println("3. Traversal");
            System.out.println("4. Size");
            System.out.println("5. Is Empty");
            System.out.println("6. Exit");

            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter items to enqueue (separated by space): ");
                String[] items = scanner.nextLine().split("\\s+");
                queue.enqueue(items);
                System.out.println("Items enqueued successfully");
            } else if (choice.equals("2")) {
                String item = queue.dequeue();
                if (item != null) {
                    System.out.println("Dequeued item: " + item);
                } else {
                    System.out.println("Queue is empty");
                }
            } else if (choice.equals("3")) {
                List<String> items = queue.traversal();
                if (!items.isEmpty()) {
                    System.out.println("Queue traversal: " + String.join(", ", items));
                } else {
                    System.out.println("Queue is empty");
                }
            } else if (choice.equals("4")) {
                System.out.println("Queue size: " + queue.size());
            } else if (choice.equals("5")) {
                if (queue.isEmpty()) {
                    System.out.println("Queue is empty");
                } else {
                    System.out.println("Queue is not empty");
                }
            } else if (choice.equals("6")) {
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }
}
