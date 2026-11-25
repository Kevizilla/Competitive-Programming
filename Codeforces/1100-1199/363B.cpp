n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0]
for i in arr:
    prefix.append(prefix[-1] + i)

minimum = float('inf')
l = 0
r = k-1
ans = 0
while r < n:
    cur = prefix[r+1] - prefix[l]
    if cur < minimum:
        minimum = cur
        ans = l+1
    r += 1
    l += 1

print(ans)