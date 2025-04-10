from collections import defaultdict

n = int(input())
files = [input() for _ in range(n)]

diction = defaultdict(int)

for file in files:
    a,b = file.split(".")
    diction[b] += 1

answer = sorted(diction.keys())
for key in answer:
    print(key, diction[key])

