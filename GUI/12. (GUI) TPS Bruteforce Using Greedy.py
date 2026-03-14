import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TspBruteForce:
    def __init__(self, distanceMatrix):
        self.distanceMatrix = distanceMatrix
        self.numCities = len(distanceMatrix)

    def calculateTotalDistance(self, route):
        totalDistance = 0
        for i in range(len(route) - 1):
            totalDistance += self.distanceMatrix[route[i]][route[i + 1]]
        totalDistance += self.distanceMatrix[route[-1]][route[0]]  # Return to start
        return totalDistance

    def solve(self):
        minDistance = math.inf
        optimalRoute = None
        # Generate all permutations of cities
        for perm in permutations(range(self.numCities)):
            perm = list(perm)  # Ensure perm is a list for index access
            currentDistance = self.calculateTotalDistance(perm)
            if currentDistance < minDistance:
                minDistance = currentDistance
                optimalRoute = perm
        return optimalRoute, minDistance

class TspGreedy:
    def __init__(self, distanceMatrix):
        self.distanceMatrix = distanceMatrix
        self.numCities = len(distanceMatrix)

    def findNearestCity(self, currentCity, unvisitedCities):
        nearestCity = None
        minDistance = float('inf')
        for city in unvisitedCities:
            if self.distanceMatrix[currentCity][city] < minDistance:
                minDistance = self.distanceMatrix[currentCity][city]
                nearestCity = city
        return nearestCity

    def solve(self, startCity=0):
        visitedCities = [startCity]
        unvisitedCities = set(range(self.numCities)) - {startCity}
        totalDistance = 0
        currentCity = startCity

        while unvisitedCities:
            nearestCity = self.findNearestCity(currentCity, unvisitedCities)
            totalDistance += self.distanceMatrix[currentCity][nearestCity]
            currentCity = nearestCity
            visitedCities.append(currentCity)
            unvisitedCities.remove(currentCity)

        totalDistance += self.distanceMatrix[currentCity][startCity]
        visitedCities.append(startCity)

        return visitedCities, totalDistance

def printRoute(route, distance, algorithmName, cityNames):
    """Print the route and distance for a given algorithm."""
    routeStr = " -> ".join(cityNames[city] for city in route)
    return f"{algorithmName} Route: {routeStr}\nTotal Distance: {distance}\n"

def drawRouteGraph(route, distanceMatrix, cityNames, algorithmName, frame, startCity):
    numCities = len(route)
    cityPositions = {i: (np.cos(2 * np.pi * i / numCities), np.sin(2 * np.pi * i / numCities)) for i in range(numCities)}

    G_route = nx.DiGraph()  # Directed graph for arrows
    for i in range(len(route)):
        G_route.add_node(route[i], pos=cityPositions[route[i]])
    for i in range(len(route) - 1):
        G_route.add_edge(route[i], route[i + 1], weight=distanceMatrix[route[i]][route[i + 1]])
    G_route.add_edge(route[-1], route[0], weight=distanceMatrix[route[-1]][route[0]])  # Return to the start city

    posRoute = nx.get_node_attributes(G_route, 'pos')
    fig, ax = plt.subplots(figsize=(6, 6))

    node_colors = ['lightblue' if node != startCity else 'orange' for node in G_route.nodes()]
    nx.draw(G_route, posRoute, with_labels=True, labels={i: cityNames[i] for i in range(len(cityNames))},
            node_color=node_colors, edge_color='gray', node_size=1000, font_size=12, ax=ax, arrows=True)

    edgeLabels = {(route[i], route[i + 1]): f'{distanceMatrix[route[i]][route[i + 1]]}' for i in range(len(route) - 1)}
    edgeLabels[(route[-1], route[0])] = f'{distanceMatrix[route[-1]][route[0]]}'
    nx.draw_networkx_edge_labels(G_route, posRoute, edge_labels=edgeLabels, font_color='red', ax=ax)

    plt.title(f"{algorithmName} Route")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    return canvas

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solver (Brute-Force & Greedy)")

        # Input section
        inputFrame = tk.Frame(root)
        inputFrame.pack(side=tk.TOP, padx=10, pady=10)

        self.numCitiesLabel = tk.Label(inputFrame, text="Enter number of cities:")
        self.numCitiesLabel.grid(row=0, column=0)

        self.numCitiesEntry = tk.Entry(inputFrame)
        self.numCitiesEntry.grid(row=0, column=1)

        self.cityNamesLabel = tk.Label(inputFrame, text="Enter city names (comma-separated):")
        self.cityNamesLabel.grid(row=1, column=0)

        self.cityNamesEntry = tk.Entry(inputFrame)
        self.cityNamesEntry.grid(row=1, column=1)

        self.distanceMatrixLabel = tk.Label(inputFrame, text="Enter the distance matrix (comma-separated rows):")
        self.distanceMatrixLabel.grid(row=2, column=0, columnspan=2)

        self.distanceMatrixEntry = tk.Text(inputFrame, height=10, width=40)
        self.distanceMatrixEntry.grid(row=3, column=0, columnspan=2)

        self.solveButton = tk.Button(inputFrame, text="Solve TSP", command=self.solveTSP)
        self.solveButton.grid(row=4, column=0, columnspan=2, pady=10)

        self.outputLabel = tk.Label(inputFrame, text="", justify="left")
        self.outputLabel.grid(row=5, column=0, columnspan=2)

        self.graphFrameBruteForce = tk.Frame(root)
        self.graphFrameBruteForce.pack(side=tk.LEFT, padx=10, pady=10)

        self.graphFrameGreedy = tk.Frame(root)
        self.graphFrameGreedy.pack(side=tk.RIGHT, padx=10, pady=10)

        self.canvasBruteForce = None
        self.canvasGreedy = None

    def solveTSP(self):
        numCities = int(self.numCitiesEntry.get())
        cityNames = self.cityNamesEntry.get().split(',')
        distanceMatrixInput = self.distanceMatrixEntry.get("1.0", tk.END).strip().splitlines()
        distanceMatrix = [list(map(int, row.split(','))) for row in distanceMatrixInput]

        if self.canvasBruteForce:
            self.canvasBruteForce.get_tk_widget().destroy()
        if self.canvasGreedy:
            self.canvasGreedy.get_tk_widget().destroy()

        tspBruteForce = TspBruteForce(distanceMatrix)
        bruteForceRoute, bruteForceMinDistance = tspBruteForce.solve()
        bruteForceResult = printRoute(bruteForceRoute, bruteForceMinDistance, "Brute-Force", cityNames)

        tspGreedy = TspGreedy(distanceMatrix)
        greedyRoute, greedyMinDistance = tspGreedy.solve(startCity=0)
        greedyResult = printRoute(greedyRoute, greedyMinDistance, "Greedy", cityNames)

        self.outputLabel.config(text=bruteForceResult + "\n" + greedyResult)

        startCity = 0
        self.canvasBruteForce = drawRouteGraph(bruteForceRoute, distanceMatrix, cityNames, "Brute-Force",
                                                self.graphFrameBruteForce, startCity)
        self.canvasGreedy = drawRouteGraph(greedyRoute, distanceMatrix, cityNames, "Greedy", self.graphFrameGreedy, startCity)

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
