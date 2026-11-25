import sys


_data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0

n = _data[idx]; idx += 1
q = _data[idx]; idx += 1

a = _data[idx:idx + n]; idx += n  # original array

# Difference array to count how many queries cover each index
diff = [0] * (n + 1)
for _ in range(q):
	l = _data[idx] - 1  # convert to 0-based
	r = _data[idx + 1] - 1  # convert to 0-based
	idx += 2
	diff[l] += 1  # mark start
	diff[r + 1] -= 1  # mark end (exclusive)

# Prefix sum to obtain coverage counts per index
for i in range(1, n + 1):
	diff[i] += diff[i - 1]

cnt = diff[:-1]  # discard sentinel

a.sort()  # sort values ascending
cnt.sort()  # sort counts ascending

ans = 0
for i in range(n):
	ans += a[i] * cnt[i]  # pair largest with largest implicitly

print(ans)

