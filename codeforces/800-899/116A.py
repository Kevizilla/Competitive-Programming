// Problem: A. Tram
// Platform: codeforces
// Contest: 800
// Rating/Difficulty: 800
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/116/A
// Solved on: 2026-11-25T05:27:55.839Z

n = int(input())
cur = mx = 0
for _ in range(n):
    a, b = map(int, input().split())
    cur += b - a
    mx = max(mx, cur)
print(mx)