
# BFS - Breadth First Search

def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()


# Test Case 1: Connected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
print("Test Case 1 - Connected Graph")
bfs(graph, 'A')
# Output: A B C D E F


# Test Case 2: Multiple Branches
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A', 'H', 'I'],
    'E': ['B'],
    'F': ['B', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['D', 'K'],
    'J': ['F'],
    'K': ['I']
}
print("Test Case 2 - Multiple Branches")
bfs(graph, 'A')
# Output: A B C D E F G H I J K


# Test Case 3: Cyclic Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'D']
}
print("Test Case 3 - Cyclic Graph")
bfs(graph, 'A')
# Output: A B C D E


# Test Case 4: Single Node
graph = {'A': []}
print("Test Case 4 - Single Node")
bfs(graph, 'A')
# Output: A


# Test Case 5: Disconnected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}
print("Test Case 5 - Disconnected Graph")
bfs(graph, 'A')
# Output: A B C






# DFS - Depth First Search

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


# Test Case 1: Connected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
print("Test Case 1 - Connected Graph")
dfs(graph, 'A', set())
print()
# Output: A B D E C F


# Test Case 2: Multiple Branches
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A', 'H', 'I'],
    'E': ['B'],
    'F': ['B', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['D', 'K'],
    'J': ['F'],
    'K': ['I']
}
print("Test Case 2 - Multiple Branches")
dfs(graph, 'A', set())
print()
# Output: A B E F J C G D H I K


# Test Case 3: Cyclic Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'D']
}
print("Test Case 3 - Cyclic Graph")
dfs(graph, 'A', set())
print()
# Output: A B D E C


# Test Case 4: Single Node
graph = {'A': []}
print("Test Case 4 - Single Node")
dfs(graph, 'A', set())
print()
# Output: A


# Test Case 5: Disconnected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}
print("Test Case 5 - Disconnected Graph")
dfs(graph, 'A', set())
print()
# Output: A B C
