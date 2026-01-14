t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if len(s) <= 10:
        print(s)
    else:
        print(f"{s[0]}{n-2}{s[-1]}")