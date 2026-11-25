// Problem: B. Bad Boy
// Platform: codeforces
// Contest: 900
// Rating/Difficulty: 900
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1537/B
// Solved on: 2026-11-25T15:00:07.426Z


t = int(input())

for _ in range(t):
    n, m, i, j = map(int, input().split())

    d1 = abs(i - 1) + abs(j - 1)
    d2 = abs(i - n) + abs(j - m)

    d3 = abs(i - 1) + abs(j - m)
    d4 = abs(i - n) + abs(j - 1)

    if d1 + d2 >= d3 + d4:
        print(1, 1, n, m)
    else:
        print(1, m, n, 1)
