t = int(input())
count = 0
for _ in range(t):
    s = input().strip()
    if s == "X++" or s == "++X":
        count += 1
    else:
        count -= 1
print(count)