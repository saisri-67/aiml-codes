
# A* Search Algorithm

def aStarAlgo(start_node, stop_node, graph_nodes, h_dist):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = min(open_set, key=lambda v: g[v] + h_dist.get(v, 0))

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            print("Total cost:", g[stop_node])
            return path, g[stop_node]

        open_set.remove(n)
        closed_set.add(n)

        for m, weight in graph_nodes.get(n, []):
            new_cost = g[n] + weight

            if m not in g or new_cost < g[m]:
                g[m] = new_cost
                parents[m] = n
                if m in closed_set:
                    closed_set.remove(m)
                open_set.add(m)

    print("Path doesn't exist")
    return None, float('inf')


# Test Case 1: Normal graph
graph_nodes = {
    'S': [('A', 2), ('B', 4)],
    'A': [('C', 2)],
    'B': [('C', 1)],
    'C': [('G', 3)],
    'G': []
}
h_dist = {'S': 5, 'A': 4, 'B': 2, 'C': 2, 'G': 0}
print("\nTest Case 1")
aStarAlgo('S', 'G', graph_nodes, h_dist)
# Output: Path found: ['S', 'A', 'C', 'G']
# Total cost: 7


# Test Case 2: Multiple possible paths
graph_nodes = {
    'S': [('A', 2), ('B', 1)],
    'A': [('G', 5)],
    'B': [('C', 2)],
    'C': [('G', 2)],
    'G': []
}
h_dist = {'S': 4, 'A': 4, 'B': 3, 'C': 1, 'G': 0}
print("\nTest Case 2")
aStarAlgo('S', 'G', graph_nodes, h_dist)
# Output: Path found: ['S', 'B', 'C', 'G']
# Total cost: 5


# Test Case 3: Start node is the goal
graph_nodes = {'S': [('G', 4)], 'G': []}
h_dist = {'S': 4, 'G': 0}
print("\nTest Case 3")
aStarAlgo('S', 'S', graph_nodes, h_dist)
# Output: Path found: ['S']
# Total cost: 0


# Test Case 4: Goal is unreachable
graph_nodes = {
    'S': [('A', 2)],
    'A': [],
    'G': []
}
h_dist = {'S': 2, 'A': 1, 'G': 0}
print("\nTest Case 4")
aStarAlgo('S', 'G', graph_nodes, h_dist)
# Output: Path doesn't exist


# Test Case 5: Direct path
graph_nodes = {
    'S': [('G', 3), ('A', 1)],
    'A': [('G', 5)],
    'G': []
}
h_dist = {'S': 3, 'A': 4, 'G': 0}
print("\nTest Case 5")
aStarAlgo('S', 'G', graph_nodes, h_dist)
# Output: Path found: ['S', 'G']
# Total cost: 3
