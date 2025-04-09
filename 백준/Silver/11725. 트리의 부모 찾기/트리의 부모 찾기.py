from collections import defaultdict, deque

n = int(input())
dict = defaultdict(list)

for _ in range(1, n):
    i,j = tuple(map(int, input().split()))
    dict[i].append(j)
    dict[j].append(i)


visited = set()
queue = deque()
queue.append(1)
answer = [0 for _ in range(n + 1)]
while queue:
    node = queue.popleft()
    for neighbor in dict[node]:
        if neighbor not in visited:
            answer[neighbor] = node
            visited.add(neighbor)
            queue.append(neighbor)

for i in range(2, n + 1):
    print(answer[i])