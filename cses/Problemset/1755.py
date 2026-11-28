// Problem: Task
// Platform: cses
// Language: unknown
// Verdict: ACCEPTED
// URL: https://cses.fi/problemset/result/19216831/
// Solved on: 2026-11-28T09:47:25.661Z

s = input()
fq = {}

for i in s:
    fq[i] = fq.get(i, 0) + 1

odd_chars = [i for i in fq if fq[i] % 2]

if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    left = ""
    middle = odd_chars[0] if odd_chars else ""

    for i in fq:
        left += i * (fq[i] // 2)

    print(left + middle + left[::-1])