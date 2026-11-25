t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    even = 0
    odd = 0

    for i in range(n):
        cur  = i % 2
        if cur != arr[i] % 2:
            if cur:
                even += 1
            else:
                odd += 1

    if even == odd:
        print(even)
    else:
        print(-1)
