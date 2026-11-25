// Problem: 2170B
// Platform: codeforces
// Language: Python3
// Verdict: Accepted
// URL: 
// Solved on: 2026-11-25T05:28:38.201Z

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    z = arr.count(0)
    # maximum = max(arr)
    s = sum(arr)

    print(min(s-n+1, n-z))

