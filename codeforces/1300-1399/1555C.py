// Problem: C. Coin Rows
// Platform: codeforces
// Contest: 1300
// Rating/Difficulty: 1300
// Language: unknown
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1555/C
// Solved on: 2026-11-25T08:39:34.964Z

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prefix_a = []
    prefix_b = []

    cur = 0
    for x in a:
        cur += x
        prefix_a.append(cur)

    cur = 0
    for x in b:
        cur += x
        prefix_b.append(cur)

    ans = float('inf')

    for i in range(n):
        bottom = prefix_b[i-1] if i > 0 else 0
        top = prefix_a[n-1] - prefix_a[i]

        bob = max(bottom, top)
        ans = min(ans, bob)

    print(ans)