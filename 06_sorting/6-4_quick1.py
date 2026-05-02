# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = [7, 5, 9, 0, 3, 1, 6, 2, 5, 4, 8]

def quick_sorting1(array, start, end):
    if start >= end: # 원소가 1개인 경우에는 종료!
        return
    
    pivot = start # 피봇 인덱스는 첫 인덱스
    left = start + 1 # 시작 인덱스는 두번째 인덱스
    right = end # 끝 인덱스는 마지막 인덱스

    while left <= right: # left와 right가 완전 교차하지 않고 일치하는 케이스에 대해서도 아래 프로세스 진행시켜야 함. # 동일한 원소가 존재할 수 있으므로 등호 필요
        while left <= end and array[left] <= array[pivot]: # left vs. pivot 동일한 원소가 존재할 수 있으므로 등호가 필요
            left += 1 # array[left] > array[pivot] 찾을 때까지 왼쪽의 인덱스는 1씩 증가시킴!
        while right > start and array[right] >= array[pivot]: # right vs. pivot 동일한 원소가 존재할 수 있으므로 등호가 필요
            right -= 1 # array[right] < array[pivot] 찾을 때까지 왼쪽의 인덱스는 1씩 증가시킴!
        if left > right: # left, right 가 엇갈림
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면, left, right 값 바꿈
            array[right], array[left] = array[left], array[right]
    
    quick_sorting1(array, start, right - 1) # pivot 과 right가 바뀌어서, right 자리에 pivot 이 들어가 있음
    quick_sorting1(array, right + 1, end) # pivot 과 right가 바뀌어서, right 자리에 pivot 이 들어가 있음

quick_sorting1(array, 0, len(array) - 1)
print(array)

