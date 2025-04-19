N = int(input())
T = []
P = []
for i in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)

dp_arr = [0 for _ in range(N + 1)]
for i in range(N):
    dp_arr[i] = max(dp_arr[i], dp_arr[i-1])
    if (i + T[i]) < N + 1:
        dp_arr[(i + T[i])] = max(dp_arr[(i + T[i])], dp_arr[i] + P[i])

print(max(dp_arr[-1], dp_arr[-2]))