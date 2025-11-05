t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    if any(a[i] >= a[i+1] for i in range(m-1)):
        print(1)
    else:
        print(n - max(a) + 1)