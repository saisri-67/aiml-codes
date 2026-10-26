
# Travelling Salesman Problem (TSP)

from itertools import permutations

def tsp(dist):
    cities = len(dist)
    start = 0
    min_cost = float('inf')
    best_path = []

    for path in permutations(range(1, cities)):
        cost = 0
        k = start

        for city in path:
            cost += dist[k][city]
            k = city

        cost += dist[k][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(path) + [start]

    print("Optimal path:", best_path)
    print("Minimum cost:", min_cost)


# Test Case 1: Four-city graph
print("Test Case 1:")
tsp([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])
# Output:
# Optimal path: [0, 1, 3, 2, 0]
# Minimum cost: 80


# Test Case 2: Triangle graph
print("\nTest Case 2:")
tsp([
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
])
# Output:
# Optimal path: [0, 1, 2, 0]
# Minimum cost: 45


# Test Case 3: Four-city graph with different costs
print("\nTest Case 3:")
tsp([
    [0, 10, 15, 20],
    [10, 0, 25, 30],
    [15, 25, 0, 35],
    [20, 30, 35, 0]
])
# Output:
# Optimal path: [0, 1, 2, 3, 0]
# Minimum cost: 90


# Test Case 4: One-city graph
print("\nTest Case 4:")
tsp([[0]])
# Output:
# Optimal path: [0, 0]
# Minimum cost: 0
