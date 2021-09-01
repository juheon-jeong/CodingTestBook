n = int(input())

line = list(map(int, input().split()))

d = [0] * 100

d[0] = line[0]
d[1] = line[1]

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + line[i])

print(d[n - 1])