n = int(input())
x1, x2 = 1, 1
plans = input().split()

# print(n, x, y, plans)

# L R U D
dx1 = (0, 0, -1, 51)
dx2 = (-1, 1, 0, 0)
moves = ('L', 'R', 'U', 'D')

for each in plans:
    for idx in range(len(moves)):
        if each == moves[idx]:
            nx1 = x1 + dx1[idx]
            nx2 = x2 + dx2[idx]
            break
    if nx1 < 1 or nx1 > n or nx2 < 1 or nx2 > n:
        continue
    else:
        x1, x2 = nx1, nx2
        print(x1, x2)
print(x1, x2)

