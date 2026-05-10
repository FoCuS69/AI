def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def kruskal(edges, n):

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    cost = 0

    print("Edges in MST:")

    for u, v, w in edges:

        pu = find(parent, u)
        pv = find(parent, v)

        if pu != pv:
            parent[pu] = pv
            cost += w

            print(u, "-", v, "=", w)

    print("Minimum Cost =", cost)

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for _ in range(e):

    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    edges.append((u, v, w))

kruskal(edges, n)
