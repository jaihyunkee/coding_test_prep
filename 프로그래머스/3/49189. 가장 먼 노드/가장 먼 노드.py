from collections import deque, defaultdict

def solution(n, edge):
    neighbors = defaultdict(list)
    for ed in edge:
        x,y = ed[0], ed[1]
        neighbors[x].append(y)
        neighbors[y].append(x)
    
    queue = deque()
    visited = set()
    queue.append((1,0))
    visited.add(1)
    ans = defaultdict(int)
    max_lvl = 0
    while queue:
        cur, lvl = queue.popleft()
        ans[lvl] += 1
        for neighbor in neighbors[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, lvl + 1))
        max_lvl = max(max_lvl, lvl)
        
    return ans[max_lvl]
            
    
    