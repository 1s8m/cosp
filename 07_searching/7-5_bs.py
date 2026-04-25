def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = 5
array = [8, 3, 7, 9, 2]
array.sort()

m = 3
x = [5, 7, 9]

# # binary search
# for i in x:
#     if binary_search(array, i, 0, len(array)): print('yes', end=' ')
#     else: print('no', end=' ')


# # count search
# array_summary = [0] * 100001
# for i in array:
#     array_summary[i] = 1

# for i in x:
#     print('yes', end=' ') if array_summary[i] != 0 else print('no', end=' ')


# set
array_set = set(array)
for i in x:
    print('yes', end=' ') if i in array_set else print('no', end=' ')