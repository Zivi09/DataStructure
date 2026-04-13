class Node<T> {
    T data;
    Node<T> next;

    Node(T data) {
        this.data = data;
        this.next = null;
    }
}

public class SinglyLinkedList<T> {
    private Node<T> head;

    public SinglyLinkedList() {
        this.head = null;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void insertAtBeginning(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = head;
        head = newNode;
    }

    public void insertAtEnd(T data) {
        Node<T> newNode = new Node<>(data);
        if (isEmpty()) {
            head = newNode;
            return;
        }
        Node<T> current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    public T deleteAtBeginning() {
        if (isEmpty()) {
            return null;
        }
        Node<T> deletedNode = head;
        head = head.next;
        return deletedNode.data;
    }

    public T deleteAtEnd() {
        if (isEmpty()) {
            return null;
        }
        if (head.next == null) {
            Node<T> deletedNode = head;
            head = null;
            return deletedNode.data;
        }
        Node<T> current = head;
        while (current.next.next != null) {
            current = current.next;
        }
        Node<T> deletedNode = current.next;
        current.next = null;
        return deletedNode.data;
    }

    public void traverse() {
        Node<T> current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        SinglyLinkedList<Integer> linkedList = new SinglyLinkedList<>();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Insert at Beginning");
            System.out.println("2. Insert at End");
            System.out.println("3. Delete from Beginning");
            System.out.println("4. Delete from End");
            System.out.println("5. Traverse");
            System.out.println("6. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                System.out.print("Enter value: ");
                try {
                    linkedList.insertAtBeginning(Integer.parseInt(scanner.nextLine()));
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("2")) {
                System.out.print("Enter value: ");
                try {
                    linkedList.insertAtEnd(Integer.parseInt(scanner.nextLine()));
                } catch (Exception e) {
                    System.out.println("Invalid input.");
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
