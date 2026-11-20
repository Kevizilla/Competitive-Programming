t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    fq = {0:1}
    ans = 0
    prefix = 0
    l  = 1

    for i in s:
        prefix += int(i)

        ans += fq.get(prefix - l, 0)
        fq[prefix - l] = fq.get(prefix - l, 0) + 1
        l += 1
    print(ans)
