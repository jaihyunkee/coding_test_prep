def solution(nums):
    temp = set(nums)
    tlen = len(temp)
    half = len(nums) // 2
    
    return min(half, tlen)