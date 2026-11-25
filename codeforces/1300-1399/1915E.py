// Problem: E. Romantic Glasses
// Platform: codeforces
// Contest: 1300
// Rating/Difficulty: 1300
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1915/E?utm_source=chatgpt.com
// Solved on: 2026-11-25T09:25:22.724Z

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