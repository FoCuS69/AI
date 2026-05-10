from collections import deque

def bfs(g, start):
    visited = set()
    q = deque([start])

    visited.add(start)

    print("BFS:", end=" ")

    while q:
        n = q.popleft()
        print(n, end=" ")

        for i in g.get(n, []):
            if i not in visited:
                visited.add(i)
                q.append(i)

def dfs(g, node, visited):
    visited.add(node)
    print(node, end=" ")

    for i in g.get(node, []):
        if i not in visited:
            dfs(g, i, visited)

v = int(input("Number of Vertices: "))
e = int(input("Number of Edges: "))

g = {}

print("Enter edges connected:")

for _ in range(e):
    u, w = map(int, input().split())

    if u not in g:
        g[u] = []

    if w not in g:
        g[w] = []

    g[u].append(w)
    g[w].append(u)

start = int(input("Start vertex: "))

bfs(g, start)

print("\nDFS:", end=" ")
visited = set()
dfs(g, start, visited)
