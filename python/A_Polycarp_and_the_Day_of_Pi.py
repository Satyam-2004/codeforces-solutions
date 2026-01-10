t = int(input())
for _ in range(t):
    s = input().strip()
    count = 0
    pi = "314159265358979323846264338327"
    for i in range(len(s)):
        if s[i] == pi[i]:
            count += 1
        else:
            break
    
    print(count)