n = int(input("Enter number of nodes: "))

nodes = []
for i in range(n):
    nodes.append(input("Enter node name: "))

print("Enter Adjacency Matrix:")

g = [list(map(int, input().split())) for _ in range(n)]

degree = [sum(i) for i in g]

sorted_nodes = [x for _, x in sorted(zip(degree, nodes), reverse=True)]

colors = {}
available = ["Red", "Blue", "Green", "Yellow"]

for node in sorted_nodes:

    i = nodes.index(node)

    used = set()

    for j in range(n):
        if g[i][j] == 1 and nodes[j] in colors:
            used.add(colors[nodes[j]])

    for c in available:
        if c not in used:
            colors[node] = c
            break

print("\nGraph Coloring:")

for node in nodes:
    print(node, "=", colors[node])
