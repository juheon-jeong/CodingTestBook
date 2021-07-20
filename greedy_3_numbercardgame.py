n, m = map(int, input().split())

min_list = []
list_1 = [[0] * m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        list_1[i][j] = temp[j]
    min_list.append(min(list_1[i]))

print(max(min_list))
