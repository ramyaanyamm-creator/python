INF = 9999  # Number used to represent no direct link

# Number of nodes
n = int(input("Enter number of nodes: "))

# Initialize distance matrix
graph = []

print("\nEnter the delay/cost between nodes")
print("Enter 0 for same node and 9999 if there is no direct link.\n")

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    graph.append(row)

# Distance vector table
distance = [row[:] for row in graph]

# Next hop table
next_hop = [[-1] * n for _ in range(n)]

# Initialize next hop
for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] != INF:
            next_hop[i][j] = j

# Distance Vector Algorithm
updated = True

while updated:
    updated = False

    for i in range(n):
        for j in range(n):
            for k in range(n):

                if distance[i][k] != INF and graph[k][j] != INF:
                    new_distance = distance[i][k] + graph[k][j]

                    if new_distance < distance[i][j]:
                        distance[i][j] = new_distance
                        next_hop[i][j] = next_hop[i][k]
                        updated = True

# Display routing tables
print("\n========== ROUTING TABLES ==========")

for i in range(n):
    print(f"\nRouting Table for Node {i + 1}")
    print("--------------------------------")
    print("Destination\tCost\tNext Hop")

    for j in range(n):
        if i == j:
            print(f"{j + 1}\t\t0\t-")

        elif distance[i][j] == INF:
            print(f"{j + 1}\t\tINF\t-")

        else:
            print(
                f"{j + 1}\t\t{distance[i][j]}\t{next_hop[i][j] + 1}"
            )
