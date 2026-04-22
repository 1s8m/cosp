array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i 부터 0+1 까지 1씩 감소
        if array[j] < array[j-1]: # 앞은 무조건 정렬이 되어 있다는 가정인데, 앞에 원소가 더 클 경우
            array[j], array[j-1] = array[j-1], array[j]
        else: # 앞은 무조건 정렬이 되어 있다는 가정인데, 제대로 정렬이 된 걸 찾았다! = 이후로는 무조건 정렬이 잘 되어 있을 것이라 중지
            break

print(array)