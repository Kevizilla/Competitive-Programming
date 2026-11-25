// Problem: A. Ultra-Fast Mathematician
// Platform: codeforces
// Contest: 800
// Rating/Difficulty: 800
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/61/A
// Solved on: 2026-11-25T10:11:56.317Z

a = input().strip()
b = input().strip()
print("".join("1" if x != y else "0" for x, y in zip(a, b)))