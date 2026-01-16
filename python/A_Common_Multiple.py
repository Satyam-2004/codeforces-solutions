t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    length = len(set(s))
    print(length)