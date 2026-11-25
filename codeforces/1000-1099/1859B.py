// Problem: B. Olya and Game with Arrays
// Platform: codeforces
// Contest: 1000
// Rating/Difficulty: 1000
// Language: Python3
// Verdict: Accepted
// URL: https://codeforces.com/problemset/problem/1859/B?utm_source=chatgpt.com
// Solved on: 2026-11-25T19:22:33.510Z


t = int(input())

for _ in range(t):
    n = int(input())

    mins = []
    seconds = []

    for _ in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        mins.append(arr[0])
        seconds.append(arr[1])

    ans = sum(seconds) - min(seconds) + min(mins)

    print(ans)
