// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19217575/
// Solved on: 2026-11-28T09:48:24.077Z

n = int(input())arr = list(map(int, input().split())) p_1 = 0p_2 = 1longest = 1cur = 1window = {arr[0]} while p_2 < n:    if arr[p_2] not in window:        window.add(arr[p_2])        cur += 1        p_2 += 1    else:        longest = max(longest, cur)        while arr[p_1] != arr[p_2]:            window.remove(arr[p_1])            p_1 += 1            cur -= 1        window.remove(arr[p_1])        p_1 += 1        cur-= 1longest = max(longest, cur)print(longest)