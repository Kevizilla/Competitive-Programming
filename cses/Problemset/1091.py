// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19292910/
// Solved on: 2026-11-28T09:48:08.503Z

import sysfrom bisect import bisect_right input = sys.stdin.readline n, m = map(int, input().split())prices = sorted(map(int, input().split()))bids = list(map(int, input().split())) # parent[i] = index of the largest unused ticket at position <= i (shifted by 1; 0 means none)parent = list(range(n + 1)) def find(x):    root = x    while parent[root] != root:        root = parent[root]    while parent[x] != root:        parent[x], x = root, parent[x]    return root out = []for b in bids:    pos = bisect_right(prices, b)   # number of tickets with price <= b    idx = find(pos)                 # largest unused among first `pos` tickets    if idx == 0:        out.append(-1)    else:        out.append(prices[idx - 1])        parent[idx] = idx - 1       # remove this ticketprint("\n".join(map(str, out)))