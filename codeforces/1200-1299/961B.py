// Problem: B. Lecture Sleep
// Platform: codeforces
// Contest: 1200
// Rating/Difficulty: 1200
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/961/B
// Solved on: 2026-11-25T20:05:42.993Z

n, k = map(int, input().split())

lectures = list(map(int, input().split()))
sleep = list(map(int, input().split()))

prefix = [0]
cur = 0
ans = 0

for i, j in zip(sleep, lectures):
    if i == 1:
        ans += j
        prefix.append(cur)
    else:
        prefix.append(cur + j)
        cur += j

pointer_1 = 0
pointer_2 = k-1
maximum = 0

while pointer_2 < n:
    cur_sum = prefix[pointer_2+1] - prefix[pointer_1]
    maximum = max(maximum, cur_sum)
    pointer_2 += 1
    pointer_1 += 1

print(maximum + ans)
