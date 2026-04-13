import java.util.*;

public class Graph {
    private Map<String, List<String>> adjList;

    public Graph() {
        this.adjList = new HashMap<>();
    }

    public void addVertex(String vertex) {
        if (!adjList.containsKey(vertex)) {
            adjList.put(vertex, new ArrayList<>());
            System.out.println("Vertex '" + vertex + "' added.");
        } else {
            System.out.println("Vertex '" + vertex + "' already exists.");
        }
    }

    public void addEdge(String vertex1, String vertex2) {
        if (adjList.containsKey(vertex1) && adjList.containsKey(vertex2)) {
            if (!adjList.get(vertex1).contains(vertex2)) {
                adjList.get(vertex1).add(vertex2);
            }
            if (!adjList.get(vertex2).contains(vertex1)) {
                adjList.get(vertex2).add(vertex1);
            }
            System.out.println("Edge between '" + vertex1 + "' and '" + vertex2 + "' added.");
        } else {
            System.out.println("One or both vertices not found.");
        }
    }

    public void removeVertex(String vertex) {
        if (adjList.containsKey(vertex)) {
            for (String otherVertex : adjList.get(vertex)) {
                adjList.get(otherVertex).remove(vertex);
            }
            adjList.remove(vertex);
            System.out.println("Vertex '" + vertex + "' removed.");
        } else {
            System.out.println("Vertex '" + vertex + "' does not exist.");
        }
    }

    public void removeEdge(String vertex1, String vertex2) {
        if (adjList.containsKey(vertex1) && adjList.containsKey(vertex2)) {
            adjList.get(vertex1).remove(vertex2);
            adjList.get(vertex2).remove(vertex1);
            System.out.println("Edge between '" + vertex1 + "' and '" + vertex2 + "' removed.");
        } else {
            System.out.println("One or both vertices not found.");
        }
    }

    public void displayGraph() {
        for (Map.Entry<String, List<String>> entry : adjList.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        Graph graph = new Graph();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nGraph Operations Menu:");
            System.out.println("1. Add Vertex");
            System.out.println("2. Add Edge");
            System.out.println("3. Remove Vertex");
            System.out.println("4. Remove Edge");
            System.out.println("5. Display Graph");
            System.out.println("6. Exit");

            System.out.print("Enter your choice (1-6): ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter vertex to add: ");
                graph.addVertex(scanner.nextLine());
            } else if (choice.equals("2")) {
                System.out.print("Enter first vertex of the edge: ");
                String v1 = scanner.nextLine();
                System.out.print("Enter second vertex of the edge: ");
                String v2 = scanner.nextLine();
                graph.addEdge(v1, v2);
            } else if (choice.equals("3")) {
                System.out.print("Enter vertex to remove: ");
                graph.removeVertex(scanner.nextLine());
            } else if (choice.equals("4")) {
                System.out.print("Enter first vertex of the edge to remove: ");
                String v1 = scanner.nextLine();
                System.out.print("Enter second vertex of the edge to remove: ");
                String v2 = scanner.nextLine();
                graph.removeEdge(v1, v2);
            } else if (choice.equals("5")) {
                System.out.println("Current Graph:");
                graph.displayGraph();
            } else if (choice.equals("6")) {
                System.out.println("Exiting...");
                break;
            } else {
                System.out.println("Invalid choice. Please enter a number between 1 and 6.");
            }
        }
        scanner.close();
    }
}
