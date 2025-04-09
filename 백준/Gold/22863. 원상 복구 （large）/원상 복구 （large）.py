from collections import defaultdict

n,k = map(int,input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

visited = [False] * n
result = [0] * n

for i in range(n):
    if not visited[i]:
        # 사이클 찾기
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = d[current] - 1
        
        cycle_len = len(cycle)
        for idx in range(cycle_len):
            new_idx = (idx + k) % cycle_len
            # cycle[new_idx] = 들어가야하는자리
            # cycle[idx] = 들어갈 숫자 from s
            result[cycle[new_idx]] = s[cycle[idx]]
print(*result)
