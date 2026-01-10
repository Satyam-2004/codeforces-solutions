t = int(input())
for _ in range(t):
    s = int(input())

    if s % 2 != 0:
        print(0)
    else:
        res = (s // 4) + 1
        print(res)