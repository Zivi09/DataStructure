import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class CustomPriorityQueue<T> {
    private static class Element<T> implements Comparable<Element<T>> {
        int priority;
        T item;

        Element(int priority, T item) {
            this.priority = priority;
            this.item = item;
        }

        @Override
        public int compareTo(Element<T> other) {
            return Integer.compare(this.priority, other.priority);
        }
    }

    private PriorityQueue<Element<T>> queue;

    public CustomPriorityQueue() {
        this.queue = new PriorityQueue<>();
    }

    public void insert(T[] items, int[] priorities) {
        for (int i = 0; i < Math.min(items.length, priorities.length); i++) {
            queue.add(new Element<>(priorities[i], items[i]));
        }
    }

    public int size() {
        return queue.size();
    }

    public T dequeue() {
        if (isEmpty()) {
            return null;
        }
        return queue.poll().item;
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public List<T> traversal() {
        List<T> items = new ArrayList<>();
        // PriorityQueue doesn't guarantee order during iteration, 
        // matches Python's traversal of the underlying heap array.
        for (Element<T> element : queue) {
            items.add(element.item);
        }
        return items;
    }

    public static void main(String[] args) {
        CustomPriorityQueue<String> queue = new CustomPriorityQueue<>();
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
                System.out.print("Enter items (separated by space): ");
                String[] items = scanner.nextLine().split("\\s+");
                System.out.print("Enter priorities (separated by space): ");
                String[] priorityStrings = scanner.nextLine().split("\\s+");
                int[] priorities = new int[priorityStrings.length];
                for (int i = 0; i < priorityStrings.length; i++) {
                    priorities[i] = Integer.parseInt(priorityStrings[i]);
                }
                queue.insert(items, priorities);
                System.out.println("Items enqueued successfully");
            } else if (choice.equals("2")) {
                String item = queue.dequeue();
                if (item != null) {
                    System.out.println("Dequeue item: " + item);
                } else {
                    System.out.println("Priority queue is empty");
                }
            } else if (choice.equals("3")) {
                List<String> items = queue.traversal();
                if (!items.isEmpty()) {
                    System.out.println("Priority queue traversal: " + String.join(", ", items));
                } else {
                    System.out.println("Priority queue is empty");
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
