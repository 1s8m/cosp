
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sorting2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗값
    tail = array[1:] # 피벗 제외한 소팅 대상 리스트

    left_side = [x for x in tail if x <= pivot] # 피봇보다 작은 left 값을 전체 계산
    right_side = [x for x in tail if x > pivot] # 피봇보다 큰 right 값을 전체 계산

    return quick_sorting2(left_side) + [pivot] + quick_sorting2(right_side)

print(quick_sorting2(array))
