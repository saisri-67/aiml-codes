
# Graph Coloring Problem

def isSafe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graphColoring(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if isSafe(v, graph, color, c):
            color[v] = c

            if graphColoring(graph, m, color, v + 1):
                return True

            color[v] = 0

    return False


def test(graph, m):
    color = [0] * len(graph)

    if graphColoring(graph, m, color, 0):
        print("Color Assignment:")
        for i in range(len(color)):
            print("Vertex", i + 1, "-> Color", color[i])
    else:
        print("No solution exists")


# Test Case 1: Complete graph K4 with 4 colors
print("Test Case 1:")
test([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
], 4)
# Output:
# Color Assignment:
# Vertex 1 -> Color 1
# Vertex 2 -> Color 2
# Vertex 3 -> Color 3
# Vertex 4 -> Color 4


# Test Case 2: Triangle graph with 3 colors
print("\nTest Case 2:")
test([
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
], 3)
# Output:
# Color Assignment:
# Vertex 1 -> Color 1
# Vertex 2 -> Color 2
# Vertex 3 -> Color 3


# Test Case 3: Bipartite graph with 2 colors
print("\nTest Case 3:")
test([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
], 2)
# Output:
# Color Assignment:
# Vertex 1 -> Color 1
# Vertex 2 -> Color 2
# Vertex 3 -> Color 1
# Vertex 4 -> Color 2


# Test Case 4: One-vertex graph
print("\nTest Case 4:")
test([[0]], 1)
# Output:
# Color Assignment:
# Vertex 1 -> Color 1


# Test Case 5: Complete graph K4 with 3 colors
print("\nTest Case 5:")
test([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
], 3)
# Output:
# No solution exists
