def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 6, 4
parent = [idx for idx, each in enumerate(range(v+1))]
# for i in range(1, v+1):
#     parent[i] = i

union_parent(parent, 1, 4)
union_parent(parent, 2, 3)
union_parent(parent, 2, 4)
union_parent(parent, 5, 6)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()



