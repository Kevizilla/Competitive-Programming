// Problem: A. Presents
// Platform: codeforces
// Contest: 800
// Rating/Difficulty: 800
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/136/A
// Solved on: 2026-11-25T10:10:53.887Z

n = int(input())
p = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    ans[p[i] - 1] = i + 1
print(*ans)