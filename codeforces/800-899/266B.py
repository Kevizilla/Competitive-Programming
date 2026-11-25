// Problem: B. Queue at the School
// Platform: codeforces
// Contest: 800
// Rating/Difficulty: 800
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/266/B
// Solved on: 2026-11-25T05:31:30.863Z

n, t = map(int, input().split())
s = list(input().strip())
for _ in range(t):
    i = 0
    while i < n - 1:
        if s[i] == "B" and s[i + 1] == "G":
            s[i], s[i + 1] = "G", "B"
            i += 2
        else:
            i += 1
print("".join(s))