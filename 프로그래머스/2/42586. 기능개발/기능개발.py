def solution(progresses, speeds):
    n = len(progresses)
    days = [0 for _ in range(n)]
    for i in range(n):
        days[i] = (100 - progresses[i]) // speeds[i]
        
        # 나머지가 남으면 하루 뒤에 완료
        if (100 - progresses[i]) % speeds[i] != 0:
            days[i] += 1
            
    stack = []
    ans = []
    for i in range(n):
        if not stack:
            stack.append(days[i])
        else:
            if stack[0] < days[i]:
                completed = 0
                while stack:
                    stack.pop()
                    completed += 1
                ans.append(completed)
            stack.append(days[i])

    if stack:
        completed = 0
        while stack:
            stack.pop()
            completed += 1
        ans.append(completed)
    
    return ans
                    
            
            
            