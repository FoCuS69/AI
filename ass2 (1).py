from queue import PriorityQueue

start = [['1','2','3'],
         ['5','6','_'],
         ['4','7','8']]

goal = [['1','2','3'],
        ['4','5','6'],
        ['7','8','_']]

def h(s):
    return sum(s[i][j] != goal[i][j] and s[i][j] != '_'
               for i in range(3) for j in range(3))

def pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == '_':
                return i, j

pq = PriorityQueue()
pq.put((h(start), start, []))
visited = []

while not pq.empty():

    f, s, path = pq.get()

    print("\nStep", len(path))

    for r in s:
        print(*r)

    if h(s) == 0:
        print("\nGoal Reached")
        print("Moves:", " -> ".join(path))
        break

    visited.append(s)

    x, y = pos(s)

    moves = [("Right",0,1), ("Left",0,-1),
             ("Down",1,0), ("Up",-1,0)]

    for move, dx, dy in moves:

        nx, ny = x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            t = [r[:] for r in s]
            t[x][y], t[nx][ny] = t[nx][ny], t[x][y]

            if t not in visited:
                pq.put((h(t), t, path + [move]))
