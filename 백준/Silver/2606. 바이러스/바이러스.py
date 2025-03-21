from collections import deque

N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for _ in range(M)]

neighbors = {}
for edge in edges:
    a,b = edge
    if a not in neighbors.keys():
        neighbors[a] = [b]
    else:
        neighbors[a].append(b)
    if b not in neighbors.keys():
        neighbors[b] = [a]
    else:
        neighbors[b].append(a)

if 1 not in neighbors.keys():
    print(0)
else:
    # bfs
    queue = deque()
    visited = set()
    queue.append(1)
    count = -1
    while queue:
        node = queue.popleft()
        visited.add(node)
        count += 1
        for neighbor in neighbors[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    print(count)
