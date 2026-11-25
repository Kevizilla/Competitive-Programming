// Problem: C. Good Subarrays
// Platform: codeforces
// Contest: 1600
// Rating/Difficulty: 1600
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1398/C?utm_source=chatgpt.com
// Solved on: 2026-11-25T09:22:33.353Z

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    fq = {0:1}
    ans = 0
    prefix = 0
    l  = 1

    for i in s:
        prefix += int(i)

        ans += fq.get(prefix - l, 0)
        fq[prefix - l] = fq.get(prefix - l, 0) + 1
        l += 1
    print(ans)
