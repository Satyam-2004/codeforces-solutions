t = int(input())
for _ in range(t):
    s = int(input())
    if s % 4 == 0:
        print(s // 4)
    else:
        print((s // 4)+ 1)
        