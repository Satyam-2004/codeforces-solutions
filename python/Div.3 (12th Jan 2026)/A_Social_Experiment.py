t = int(input())
for _ in range(t):
    s = int(input())

    if s == 2 or s == 3:
        print(s)
    else:
        mod = s % 2
        print(mod)