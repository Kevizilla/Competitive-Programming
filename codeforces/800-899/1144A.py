t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    if len(set(s)) != n:
        print("NO")
        continue
    ascii = []
    for i in s:
        ascii.append(ord(i))
    if max(ascii) - min(ascii) == n-1:
        print("YES")
    else:
        print("NO")
