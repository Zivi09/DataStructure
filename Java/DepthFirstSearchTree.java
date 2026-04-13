import java.util.*;

public class DepthFirstSearchTree {
    private Map<String, List<String>> graph;

    public DepthFirstSearchTree() {
        this.graph = new HashMap<>();
    }

    public void addVertex(String vertex) {
        if (!graph.containsKey(vertex)) {
            graph.put(vertex, new ArrayList<>());
        }
    }

    public void addEdge(String vertex1, String vertex2) {
        if (graph.containsKey(vertex1) && graph.containsKey(vertex2)) {
            graph.get(vertex1).add(vertex2);
            graph.get(vertex2).add(vertex1);
        }
    }

    public Map<String, List<String>> dfsTree(String start) {
        Set<String> visited = new HashSet<>();
        Map<String, List<String>> dfsTree = new HashMap<>();
        java.util.Stack<String> stack = new java.util.Stack<>();

        stack.push(start);
        visited.add(start);

        while (!stack.isEmpty()) {
            String current = stack.pop();
            for (String neighbor : graph.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    dfsTree.computeIfAbsent(current, k -> new ArrayList<>()).add(neighbor);
                    stack.push(neighbor);
                }
            }
        }
        return dfsTree;
    }

    public void display() {
        for (Map.Entry<String, List<String>> entry : graph.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void printDfsTree(Map<String, List<String>> dfsTree, String start) {
        System.out.println("Depth-First Tree starting from " + start + ":");
        for (String vertex : dfsTree.keySet()) {
            System.out.println(vertex + ": " + dfsTree.get(vertex));
        }
    }

    public static void main(String[] args) {
        DepthFirstSearchTree g = new DepthFirstSearchTree();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Add Vertex");
            System.out.println("2. Add Edge");
            System.out.println("3. Run DFS Tree");
            System.out.println("4. Display Graph");
            System.out.println("5. Exit");
            System.out.print("Choice: ");
            String choice = scanner.nextLine();
            if (choice.equals("1")) {
                System.out.print("Enter vertex name: ");
                g.addVertex(scanner.nextLine());
            } else if (choice.equals("2")) {
                System.out.print("Enter first vertex: ");
                String v1 = scanner.nextLine();
                System.out.print("Enter second vertex: ");
                String v2 = scanner.nextLine();
                g.addEdge(v1, v2);
            } else if (choice.equals("3")) {
                System.out.print("Enter start vertex: ");
                String start = scanner.nextLine();
                Map<String, List<String>> tree = g.dfsTree(start);
                printDfsTree(tree, start);
            } else if (choice.equals("4")) {
                g.display();
            } else if (choice.equals("5")) {
                break;
            }
        }
        scanner.close();
    }
}
