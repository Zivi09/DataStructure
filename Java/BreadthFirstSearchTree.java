import java.util.*;

public class BreadthFirstSearchTree {
    private Map<String, List<String>> graph;

    public BreadthFirstSearchTree() {
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

    public Map<String, List<String>> bfsTree(String start) {
        Set<String> visited = new HashSet<>();
        Map<String, List<String>> bfsTree = new HashMap<>();
        java.util.Queue<String> queue = new java.util.LinkedList<>();

        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            String current = queue.poll();
            for (String neighbor : graph.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    bfsTree.computeIfAbsent(current, k -> new ArrayList<>()).add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return bfsTree;
    }

    public void display() {
        for (Map.Entry<String, List<String>> entry : graph.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void printBfsTree(Map<String, List<String>> bfsTree, String start) {
        System.out.println("Breadth-First Tree starting from " + start + ":");
        for (String vertex : bfsTree.keySet()) {
            System.out.println(vertex + ": " + bfsTree.get(vertex));
        }
    }

    public static void main(String[] args) {
        BreadthFirstSearchTree g = new BreadthFirstSearchTree();
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        while (true) {
            System.out.println("\n1. Add Vertex");
            System.out.println("2. Add Edge");
            System.out.println("3. Run BFS Tree");
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
                Map<String, List<String>> tree = g.bfsTree(start);
                printBfsTree(tree, start);
            } else if (choice.equals("4")) {
                g.display();
            } else if (choice.equals("5")) {
                break;
            }
        }
        scanner.close();
    }
}
