N = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0

# 홀수일때는 미리 하나 뺌
if N % 2 == 1:
    ans = nums[-1]
    nums = nums[:-1]
    N -= 1

# 근손실의 최적의 경우의 수의 최댓값
for i in range(N // 2):
    ans = max(ans, nums[i] + nums[N - 1 - i])

print(ans)