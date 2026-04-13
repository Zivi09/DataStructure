public class HashTableBasic {
    private int size;
    private String[] table;

    public HashTableBasic(int size) {
        this.size = size;
        this.table = new String[size];
    }

    private int hashFunction(int key) {
        return key % size;
    }

    public void insert(int key, String value) {
        int index = hashFunction(key);
        table[index] = value;
        System.out.println("Inserted: (" + key + ", " + value + ") at index " + index);
    }

    public void delete(int key) {
        int index = hashFunction(key);
        if (table[index] != null) {
            System.out.println("Deleted: (" + key + ", " + table[index] + ") from index " + index);
            table[index] = null;
        } else {
            System.out.println("Key " + key + " not found for deletion.");
        }
    }

    public void traverse() {
        System.out.println("Hash Table Contents:");
        for (int i = 0; i < size; i++) {
            if (table[i] != null) {
                System.out.println("Index " + i + ": " + table[i]);
            } else {
                System.out.println("Index " + i + ": null");
            }
        }
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter table size: ");
        int size = Integer.parseInt(scanner.nextLine());
        HashTableBasic hashTable = new HashTableBasic(size);
        while (true) {
            System.out.println("\n1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Traverse");
            System.out.println("4. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                try {
                    System.out.print("Enter key (int): ");
                    int key = Integer.parseInt(scanner.nextLine());
                    System.out.print("Enter value: ");
                    String value = scanner.nextLine();
                    hashTable.insert(key, value);
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("2")) {
                try {
                    System.out.print("Enter key to delete: ");
                    int key = Integer.parseInt(scanner.nextLine());
                    hashTable.delete(key);
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("3")) {
                hashTable.traverse();
            } else if (choice.equals("4")) {
                break;
            }
        }
        scanner.close();
    }
}
