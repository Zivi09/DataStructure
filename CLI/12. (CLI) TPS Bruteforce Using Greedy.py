from itertools import permutations
import math

class TSP:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def calculate_total_distance(self, route):
        """Calculate the total distance of a given route."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i+1]]
        # Add distance to return to the starting city
        total_distance += self.distance_matrix[route[-1]][route[0]]
        return total_distance

    def solve(self):
        """Solve the TSP using brute force."""
        min_distance = math.inf
        best_route = None
        # Generate all possible permutations of cities (excluding the starting city)
        for perm in permutations(range(self.num_cities)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return best_route, min_distance

def print_route(route, distance):
    """Print the optimal route and its distance."""
    route_str = " -> ".join(f"City {city}" for city in route)
    print(f"Optimal Route: {route_str}")
    print(f"Total Distance: {distance}")

# Example usage
if __name__ == "__main__":
    # Define a distance matrix for the cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp = TSP(distance_matrix)
    best_route, min_distance = tsp.solve()
    print_route(best_route, min_distance)
