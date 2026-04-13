import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class TSPBruteForce {
    private int[][] distanceMatrix;
    private int numCities;

    public TSPBruteForce(int[][] distanceMatrix) {
        this.distanceMatrix = distanceMatrix;
        this.numCities = distanceMatrix.length;
    }

    public double calculateTotalDistance(List<Integer> route) {
        double totalDistance = 0;
        for (int i = 0; i < route.size() - 1; i++) {
            totalDistance += distanceMatrix[route.get(i)][route.get(i + 1)];
        }
        // Add distance to return to the starting city
        totalDistance += distanceMatrix[route.get(route.size() - 1)][route.get(0)];
        return totalDistance;
    }

    public Object[] solve() {
        double minDistance = Double.POSITIVE_INFINITY;
        List<Integer> bestRoute = null;

        List<Integer> cities = new ArrayList<>();
        for (int i = 0; i < numCities; i++) cities.add(i);

        List<List<Integer>> allPermutations = new ArrayList<>();
        generatePermutations(cities, 0, allPermutations);

        for (List<Integer> perm : allPermutations) {
            double currentDistance = calculateTotalDistance(perm);
            if (currentDistance < minDistance) {
                minDistance = currentDistance;
                bestRoute = new ArrayList<>(perm);
            }
        }
        return new Object[]{bestRoute, minDistance};
    }

    private void generatePermutations(List<Integer> list, int start, List<List<Integer>> result) {
        if (start >= list.size()) {
            result.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i < list.size(); i++) {
            java.util.Collections.swap(list, start, i);
            generatePermutations(list, start + 1, result);
            java.util.Collections.swap(list, start, i);
        }
    }

    public static void printRoute(List<Integer> route, double distance) {
        String routeStr = route.stream()
                .map(city -> "City " + city)
                .collect(Collectors.joining(" -> "));
        System.out.println("Optimal Route: " + routeStr);
        System.out.println("Total Distance: " + distance);
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter numbers of cities: ");
        int n = Integer.parseInt(scanner.nextLine());
        int[][] distanceMatrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    distanceMatrix[i][j] = 0;
                    continue;
                }
                System.out.print("Distance from City " + i + " to City " + j + ": ");
                distanceMatrix[i][j] = Integer.parseInt(scanner.nextLine());
            }
        }

        TSPBruteForce tsp = new TSPBruteForce(distanceMatrix);
        Object[] result = tsp.solve();
        @SuppressWarnings("unchecked")
        List<Integer> bestRoute = (List<Integer>) result[0];
        double minDistance = (double) result[1];

        printRoute(bestRoute, minDistance);
        scanner.close();
    }
}
