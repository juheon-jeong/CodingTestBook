size = int(input())

shift = input().split(" ")

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move = ['L', 'R', 'U', 'D']


for s in shift:
    for i in range(len(move)):
        if s == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > size or ny < 1 or ny > size:
        continue
    x, y = nx, ny

print(x, y)