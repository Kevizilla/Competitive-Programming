t = int(input())

for _ in range(t):
    s = input().strip()
    a = [0] + [int(c) for c in s]

    n = len(a)
    cut = n

    for i in range(n - 1, 0, -1):
        if a[i] >= 5:
            a[i - 1] += 1
            cut = i

    for i in range(cut, n):
        a[i] = 0

    print(''.join(map(str, a)).lstrip('0'))