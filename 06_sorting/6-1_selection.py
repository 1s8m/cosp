array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # i 로 초기 min_index 임시 할당
    
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # j 인덱스가 min_index 인덱스보다 더 작은 값일 경우 (min_index 보다 적은 값의 인덱스 발견!)
            min_index = j
        
    # i 이후의 모든 원소들에 대해서 가장 적은 값을 찾았다.
    array[i], array[min_index] = array[min_index], array[i]

print(array)