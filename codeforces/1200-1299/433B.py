// Problem: B. Kuriyama Mirai's Stones
// Platform: codeforces
// Contest: 1200
// Rating/Difficulty: 1200
// Language: unknown
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/433/B
// Solved on: 2026-11-25T09:17:29.863Z

n = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0]
for i in arr:
    prefix.append(prefix[-1] + i)

arr.sort()

sorted_prefix = [0]
for i in arr:
    sorted_prefix.append(sorted_prefix[-1] + i)

q = int(input())
for _ in range(q):
    type, l, r = map(int, input().split())
    if type == 1:
        print(prefix[r] - prefix[l-1])
    else:
        print(sorted_prefix[r] - sorted_prefix[l-1])

