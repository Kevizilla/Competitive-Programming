import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = [0]
    s = 0

    for i in range(n):
        if i % 2 == 0:
            s += a[i]
        else:
            s -= a[i]

        prefix.append(s)

    prefix.sort()

    found = False

    for i in range(1, len(prefix)):
        if prefix[i] == prefix[i - 1]:
            found = True
            break

    print("YES" if found else "NO")