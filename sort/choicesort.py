array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#선택정렬
#매 인덱스마다 가장 작은 원소를 찾아 스왑

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


print(array)