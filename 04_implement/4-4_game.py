n, m = map(int, input().split())

x1, x2, direction = map(int, input().split())
# direction: 북 동 남 서 0 1 2 3

d = [[0]*n for _ in range(m)]
d[x1][x2] = 0

# 북 동 남 서
dx1 = (-1, 0, 1, 0)
dx2 = (0, 1, 0, -1)

jido = []
for i in range(n):
    jido.append(list(map(int, input().split())))

# print(n, m)
# print(x1, x2, direction)
# print(jido)
# print(d)

def turn_left():
    global direction
    direction -= 1
    if direction < 0: direction = 3

# print(direction)
# turn_left()
# print(direction)

visit_count = 1
turn_times = 0

while True:
    turn_left() # 왼쪽 회전 
    nx1 = x1 + dx1[direction]
    nx2 = x2 + dx2[direction]

    # 회전한 방향 앞 칸에 방문해봤냐?
    if d[nx1][nx2] == 0 and jido[nx1][nx2] == 0:
        d[nx1][nx2] = 1
        x1, x2 = nx1, nx2
        visit_count += 1
        turn_times = 0
        continue
    # 회전한 방향 앞 칸이 없거나 방문 다 했다.
    else:
        turn_times += 1
    
    # 0, 1, 2, 3 turn_times 거치고 방향이 원래 방향으로 돌아옴
    if turn_times == 4: # 4방향 다 봤다.
        nx1 = x1 - dx1[direction]
        nx2 = x2 - dx2[direction]

        if d[nx1][nx2] == 0: # 뒤가 육지라면 이동
            x1, x2 = nx1, nx2
            visit_count += 1
        else:
            break
        turn_times = 0

print(visit_count)