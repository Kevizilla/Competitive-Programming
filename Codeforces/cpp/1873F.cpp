t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    l = 0
    total = 0
    ans = 0

    for r in range(n):

        if r > 0 and h[r-1] % h[r] != 0:
            l = r
            total = 0

        total += a[r]

        while total > k:
            total -= a[l]
            l += 1

        ans = max(ans, r - l + 1)

    print(ans)
