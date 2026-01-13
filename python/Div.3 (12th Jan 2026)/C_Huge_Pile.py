from collections import deque

def solve(n, k):
    if n == k:
        return 0
    
    if k > n:
        return -1
    
    queue = deque([(n, 0)])  
    visited = {n}
    
    while queue:
        curr, divisions = queue.popleft()
        
        pile1 = curr // 2
        pile2 = (curr + 1) // 2
        
        if pile1 == k or pile2 == k:
            return divisions + 1
        
        for pile in [pile1, pile2]:
            if pile not in visited and pile >= k:
                visited.add(pile)
                queue.append((pile, divisions + 1))
    
    return -1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))