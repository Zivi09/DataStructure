import java.util.ArrayList;
import java.util.List;

public class Stack<T> {
    private List<T> items;

    public Stack() {
        this.items = new ArrayList<>();
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public void push(T data) {
        items.add(data);
    }

    public T pop() {
        if (isEmpty()) {
            return null;
        }
        return items.remove(items.size() - 1);
    }

    public T peek() {
        if (isEmpty()) {
            return null;
        }
        return items.get(items.size() - 1);
    }

    public int size() {
        return items.size();
    }

    public void printStack() {
        System.out.println("Stack elements:");
        for (int i = items.size() - 1; i >= 0; i--) {
            System.out.println(items.get(i));
        }
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Size");
            System.out.println("5. Print Stack");
            System.out.println("6. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                System.out.print("Enter value: ");
                try {
                    stack.push(Integer.parseInt(scanner.nextLine()));
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("2")) {
                Integer val = stack.pop();
                if (val != null) System.out.println("Popped: " + val);
                else System.out.println("Stack empty.");
            } else if (choice.equals("3")) {
                Integer val = stack.peek();
                if (val != null) System.out.println("Peek: " + val);
                else System.out.println("Stack empty.");
            } else if (choice.equals("4")) {
                System.out.println("Size: " + stack.size());
            } else if (choice.equals("5")) {
                stack.printStack();
            } else if (choice.equals("6")) {
                break;
            }
        }
        scanner.close();
    }
}
