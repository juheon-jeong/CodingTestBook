n, m = map(int, input().split())

x = list(map(int, input().split()))

left = 1

right = max(x)

while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in x:
        if i > mid:
            temp += (i - mid)

    if temp < m:
        right = mid - 1


    else:
        result = mid
        left = mid + 1



print(result)