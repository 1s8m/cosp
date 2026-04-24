def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # int( (start + end) / 2 )

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
# n, target = list(map(int, input().split()))
n, target = 10, 7

# array = list(map(int, input().split()))
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, 7, 0, len(array)-1)
print(result+1)




def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n, target = list(map(int, input().split()))
n, target = 10, 7

# array = list(map(int, input().split()))
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, 7, 0, len(array)-1)
print(result+1)
 