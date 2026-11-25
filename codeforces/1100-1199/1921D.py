// Problem: D. Very Different Array
// Platform: codeforces
// Contest: 1100
// Rating/Difficulty: 1100
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1921/D?utm_source=chatgpt.com
// Solved on: 2026-11-25T09:25:49.919Z

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    narr = list(map(int, input().split()))
    marr = list(map(int, input().split()))
    narr.sort()
    marr.sort()

    ans = 0
    l1, l2 = 0, 0
    r1, r2 = n - 1, m - 1

    for _ in range(min(n, m)):
        d1 = abs(narr[l1] - marr[r2])
        d2 = abs(marr[l2] - narr[r1])

        if d1 >= d2:
            ans += d1
            l1 += 1
            r2 -= 1
        else:
            ans += d2
            l2 += 1
            r1 -= 1

    print(ans)