t = int(input())
for _ in range(t):
    s = input().strip()

    if s.startswith("10"):
        exp = s[2:]
        if exp != "" and exp[0] != '0' and int(exp) >= 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")