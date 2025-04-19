import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [0] * (N + 1)  # 기차는 1번부터 N번까지

for _ in range(M):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        i, x = cmd[1], cmd[2]
        bitmask = 1 << (x - 1)
        if (train[i] & bitmask) == 0:
            train[i] += bitmask

    elif cmd[0] == 2:
        i, x = cmd[1], cmd[2]
        bitmask = 1 << (x - 1)
        if (train[i] & bitmask) != 0:
            train[i] -= bitmask

    elif cmd[0] == 3:
        i = cmd[1]
        train[i] = train[i] * 2
        if train[i] >= (1 << 20):  # 21번째 비트 잘라내기
            train[i] %= (1 << 20)

    elif cmd[0] == 4:
        i = cmd[1]
        train[i] = train[i] // 2

# 기차 상태 중복 제거
print(len(set(train[1:])))