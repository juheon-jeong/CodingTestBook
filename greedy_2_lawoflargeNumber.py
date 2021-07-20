n, m, k = map(int, input().split())
tc = list(map(int, input().split()))

tc.sort(reverse=True)

result = 0

#가장 큰수
big = tc[0]
#두번째 큰수
sec = tc[1]

count = int((m/(k+1)) * k + m % (k+1))

result = big * count + sec * (m - count)

print(result)