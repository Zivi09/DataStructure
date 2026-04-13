import java.util.ArrayList;
import java.util.List;

class BTNode {
    int val;
    BTNode left, right;

    BTNode(int key) {
        val = key;
        left = right = null;
    }
}

public class BinaryTree {
    BTNode root;

    public BinaryTree() {
        root = null;
    }

    public void insert(int key) {
        if (root == null) {
            root = new BTNode(key);
        } else {
            insertRec(root, key);
        }
    }

    private void insertRec(BTNode root, int key) {
        if (key < root.val) {
            if (root.left == null) {
                root.left = new BTNode(key);
            } else {
                insertRec(root.left, key);
            }
        } else {
            if (root.right == null) {
                root.right = new BTNode(key);
            } else {
                insertRec(root.right, key);
            }
        }
    }

    public void delete(int key) {
        root = deleteRec(root, key);
    }

    private BTNode deleteRec(BTNode root, int key) {
        if (root == null) return root;

        if (key < root.val) {
            root.left = deleteRec(root.left, key);
        } else if (key > root.val) {
            root.right = deleteRec(root.right, key);
        } else {
            if (root.left == null) return root.right;
            else if (root.right == null) return root.left;

            BTNode minLargerNode = getMin(root.right);
            root.val = minLargerNode.val;
            root.right = deleteRec(root.right, minLargerNode.val);
        }
        return root;
    }

    private BTNode getMin(BTNode node) {
        BTNode current = node;
        while (current.left != null) {
            current = current.left;
        }
        return current;
    }

    public List<Integer> inorderTraversal() {
        List<Integer> res = new ArrayList<>();
        inorderRec(root, res);
        return res;
    }

    private void inorderRec(BTNode root, List<Integer> res) {
        if (root != null) {
            inorderRec(root.left, res);
            res.add(root.val);
            inorderRec(root.right, res);
        }
    }

    public List<Integer> preorderTraversal() {
        List<Integer> res = new ArrayList<>();
        preorderRec(root, res);
        return res;
    }

    private void preorderRec(BTNode root, List<Integer> res) {
        if (root != null) {
            res.add(root.val);
            preorderRec(root.left, res);
            preorderRec(root.right, res);
        }
    }

    public List<Integer> postorderTraversal() {
        List<Integer> res = new ArrayList<>();
        postorderRec(root, res);
        return res;
    }

    private void postorderRec(BTNode root, List<Integer> res) {
        if (root != null) {
            postorderRec(root.left, res);
            postorderRec(root.right, res);
            res.add(root.val);
        }
    }

    public static void main(String[] args) {
        BinaryTree bt = new BinaryTree();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Inorder Traversal");
            System.out.println("4. Preorder Traversal");
            System.out.println("5. Postorder Traversal");
            System.out.println("6. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                System.out.print("Enter value: ");
                try {
                    bt.insert(Integer.parseInt(scanner.nextLine()));
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("2")) {
                System.out.print("Enter value: ");
                try {
                    bt.delete(Integer.parseInt(scanner.nextLine()));
                } catch (Exception e) {
                    System.out.println("Invalid input.");
                }
            } else if (choice.equals("3")) {
                System.out.println("Inorder: " + bt.inorderTraversal());
            } else if (choice.equals("4")) {
                System.out.println("Preorder: " + bt.preorderTraversal());
            } else if (choice.equals("5")) {
                System.out.println("Postorder: " + bt.postorderTraversal());
            } else if (choice.equals("6")) {
                break;
            }
        }
        scanner.close();
    }
}
