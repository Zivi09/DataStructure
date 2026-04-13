import java.util.Scanner;

class DNode<T> {
    T data;
    DNode<T> next;
    DNode<T> prev;

    DNode(T data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class DoublyLinkedList<T> {
    private DNode<T> head;
    private DNode<T> tail;

    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void insertAtBeginning(T data) {
        DNode<T> newNode = new DNode<>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
    }

    public void insertAtEnd(T data) {
        DNode<T> newNode = new DNode<>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
    }

    public T deleteAtBeginning() {
        if (isEmpty()) {
            return null;
        }
        DNode<T> deletedNode = head;
        if (head == tail) {
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        return deletedNode.data;
    }

    public T deleteAtEnd() {
        if (isEmpty()) {
            return null;
        }
        DNode<T> deletedNode = tail;
        if (head == tail) {
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        return deletedNode.data;
    }

    public void traverse() {
        DNode<T> current = head;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        DoublyLinkedList<Integer> linkedList = new DoublyLinkedList<>();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n1. Insert at Beginning");
            System.out.println("2. Insert at End");
            System.out.println("3. Delete from Beginning");
            System.out.println("4. Delete from End");
            System.out.println("5. Traverse");
            System.out.println("6. Exit");
            System.out.print("Choice: ");
            String choice = scanner.next();
            if (choice.equals("1")) {
                System.out.print("Enter value: ");
                try {
                    linkedList.insertAtBeginning(scanner.nextInt());
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                    scanner.next(); // clear buffer
                }
            } else if (choice.equals("2")) {
                System.out.print("Enter value: ");
                try {
                    linkedList.insertAtEnd(scanner.nextInt());
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                    scanner.next(); // clear buffer
                }
            } else if (choice.equals("3")) {
                Integer val = linkedList.deleteAtBeginning();
                if (val != null) System.out.println("Deleted: " + val);
                else System.out.println("List empty.");
            } else if (choice.equals("4")) {
                Integer val = linkedList.deleteAtEnd();
                if (val != null) System.out.println("Deleted: " + val);
                else System.out.println("List empty.");
            } else if (choice.equals("5")) {
                linkedList.traverse();
            } else if (choice.equals("6")) {
                break;
            }
        }
        scanner.close();
    }
}
