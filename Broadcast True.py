from collections import deque

# Number of hosts
n = int(input("Enter number of hosts: "))

# Create adjacency list
graph = [[] for _ in range(n)]

# Number of connections
edges = int(input("Enter number of connections: "))

print("\nEnter the connections between hosts:")

for i in range(edges):
    u, v = map(int, input(f"Connection {i + 1}: ").split())

    # Convert to zero-based indexing
    u -= 1
    v -= 1

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)

# Root/source host
source = int(input("\nEnter the source/root host: ")) - 1

# BFS variables
visited = [False] * n
parent = [-1] * n
queue = deque()

visited[source] = True
queue.append(source)

# BFS traversal
while queue:

    current = queue.popleft()

    for neighbor in graph[current]:

        if not visited[neighbor]:

            visited[neighbor] = True
            parent[neighbor] = current
            queue.append(neighbor)

# Display Broadcast Tree
print("\n========== BROADCAST TREE ==========")

print("Parent\tChild")
print("----------------")

for i in range(n):

    if parent[i] != -1:
        print(f"{parent[i] + 1}\t{i + 1}")

# Display broadcast paths
print("\nBroadcast paths from source:")

for i in range(n):

    if i == source:
        continue

    path = []
    current = i

    while current != -1:
        path.append(current + 1)
        current = parent[current]

    path.reverse()

    print(" -> ".join(map(str, path)))
