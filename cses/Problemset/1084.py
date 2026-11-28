// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19342279/
// Solved on: 2026-11-28T09:48:00.921Z

n, m, k = map(int, input().split())
required = list(map(int, input().split()))
sizes = list(map(int, input().split()))
ans = 0

required.sort()
sizes.sort()

a = b = 0
while a < n and b < m:
    cur_req = required[a]
    cur_size = sizes[b]
    if abs(cur_req - cur_size) <= k:
        ans += 1
        b += 1
        a += 1
    elif cur_req > cur_size:
        b+=1
    else:
        a+=1


print(ans)
