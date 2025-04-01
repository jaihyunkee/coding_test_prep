words = input()

ans = ""
inclusive = False
stack = []
temp = ""

for w in words:
    if w == '<':
        inclusive = True
    elif w == '>':
        inclusive = False
        ans = ans + temp + ">"
        temp = ""
        continue

    if inclusive:
        temp = temp + w
        while stack:
            w1 = stack.pop()
            ans = ans + w1

    elif not inclusive:
        if w != " ":
            stack.append(w)
        else:
            while stack:
                w1 = stack.pop()
                ans = ans + w1
            ans = ans + " "

while stack:
    w1 = stack.pop()
    ans = ans + w1

print(ans)
        
    
