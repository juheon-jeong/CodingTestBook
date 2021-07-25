loca = input()
row = int(loca[1])
column = ord(loca[0]) - ord('a') + 1

shift = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0

for s in shift:
    nrow = row + s[0]
    ncolumn = column + s[1]

    if nrow < 1 or nrow > 8 or ncolumn < 1 or ncolumn > 8:
        continue
    result += 1

print(result)
