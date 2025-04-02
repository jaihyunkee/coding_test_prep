n = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))

min_ = node[0]
cur = 0
for i in range(1, n):
    cur += edge[i - 1] * min_
    if min_ > node[i]:
        min_ = node[i]
print(cur)
    