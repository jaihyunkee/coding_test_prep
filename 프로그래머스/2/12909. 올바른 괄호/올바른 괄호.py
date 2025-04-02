def solution(s):
    answer = True
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
            continue
        else:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
    if stack:
        answer = False
                

    return answer