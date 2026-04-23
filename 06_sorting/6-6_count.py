array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# from collections import defaultdict

# count = defaultdict(int)

# for i in array:
#     count[i] += 1

# print(count.keys())


count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')



# from itertools import chain
# print(list(chain(*[[idx] * i for idx, i in enumerate(count)])))

