from collections import deque

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
index = (0,0)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    if 2 in grid[i]:
        index = (i, grid[i].index(2))
        break

queue = deque()
visited = set()
step = 0
queue.append((index, step))
visited.add(index)
ans = [[0 for _ in range(m)] for _ in range(n)]
while queue:
    idx, s = queue.popleft()
    cx, cy = idx
    ans[cx][cy] = s
    for i in range(4):
        x,y = cx + dx[i], cy + dy[i]
        if in_range(x,y) and grid[x][y] != 0 and (x,y) not in visited:
            visited.add((x,y))
            queue.append(((x,y), s + 1))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and (i, j) not in visited:
            ans[i][j] = -1

for i in range(n):
    print(*ans[i])