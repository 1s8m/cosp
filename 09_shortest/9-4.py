# import sys
# input = sys.stdin.readline

INF = int(1e9)

start = 1

# n, m = map(int, input().split())
n, m = 5, 7

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

graph[1][2] = 1
graph[1][3] = 1
graph[1][4] = 1
graph[2][4] = 1
graph[3][4] = 1
graph[3][5] = 1
graph[4][5] = 1

graph[2][1] = 1
graph[3][1] = 1
graph[4][1] = 1
graph[4][2] = 1
graph[4][3] = 1
graph[5][3] = 1
graph[5][4] = 1

# print(graph)

# x, k = map(int, input().split())
x, k = 4, 5

for d in range(1, n+1):
    for i in range(1, n+1):
         for j in range(1, n+1):
             graph[i][j] = min(graph[i][j], graph[i][d] + graph[d][j])

# print(graph)

distance = graph[start][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)