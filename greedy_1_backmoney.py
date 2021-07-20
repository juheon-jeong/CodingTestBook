money = int(input())

list = [500, 100, 50, 10]

result = 0

for i in list:
   result += money // i
   money = money % i

print(result)