import java.util.ArrayList;
import java.util.List;

public class AbstractDataType<T> {
    private List<T> items;

    public AbstractDataType() {
        this.items = new ArrayList<>();
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public void enqueue(T item) {
        items.add(item);
    }

    public T dequeue() {
        if (!isEmpty()) {
            return items.remove(0);
        } else {
            throw new IndexOutOfBoundsException("dequeue from empty queue");
        }
    }

    public T peek() {
        if (!isEmpty()) {
            return items.get(0);
        } else {
            throw new IndexOutOfBoundsException("peek from empty queue");
        }
    }

    public int size() {
        return items.size();
    }

    @Override
    public String toString() {
        return "Queue: " + items.toString();
    }

    public static void main(String[] args) {
        AbstractDataType<Integer> queue = new AbstractDataType<>();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Size");
            System.out.println("5. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                System.out.print("Enter item: ");
                try {
                    queue.enqueue(Integer.parseInt(scanner.nextLine()));
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number.");
                }
            } else if (choice.equals("2")) {
                try {
                    System.out.println("Dequeued: " + queue.dequeue());
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                }
            } else if (choice.equals("3")) {
                try {
                    System.out.println("Peek: " + queue.peek());
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                }
            } else if (choice.equals("4")) {
                System.out.println("Size: " + queue.size());
            } else if (choice.equals("5")) {
                break;
            }
        }
        scanner.close();
    }
}
