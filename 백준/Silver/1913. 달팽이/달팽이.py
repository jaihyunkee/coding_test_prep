n = int(input())
target = int(input())

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ii = 0

arr = [[0 for _ in range(n)] for _ in range(n)]
i, j = n // 2, n // 2

cur_num = 1
arr[i][j] = cur_num
count, turn, flag = 1, 1, 0
ans = []
while cur_num <= n ** 2:
    if cur_num == target:
        ans = [i + 1,j + 1]
    
    arr[i][j] = cur_num
    i, j = i + dx[ii], j + dy[ii]

    if count == turn:
        if flag == 1:
            turn += 1
            flag = 0
        else:
            flag = 1
        count = 0
        ii = (ii + 1) % 4

    count += 1
    cur_num += 1

for i in range(n):
    print(' '.join(map(str, arr[i])))

print(ans[0], ans[1])