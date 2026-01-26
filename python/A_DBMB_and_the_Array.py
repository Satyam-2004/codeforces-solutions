t = int(input())
for _ in range(t):
    n, s, x = map(int,input(). split())
    arr = list(map(int, input().split()))

    total = sum(arr)

    if total <= s and (s- total) % x == 0:
        print("YES")
    else:
        print("NO")