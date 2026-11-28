// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19197397/
// Solved on: 2026-11-28T09:48:15.443Z

n, target = map(int, input().split())arr = list(map(int, input().split())) arr = [(arr[i], i) for i in range(n)]arr.sort() left, right = 0, n - 1 while left < right:    total = arr[left][0] + arr[right][0]     if total == target:        print(arr[left][1] + 1, arr[right][1] + 1)        break    elif total < target:        left += 1    else:        right -= 1else:    print("IMPOSSIBLE")