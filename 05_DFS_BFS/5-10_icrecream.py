n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x1,x2):
    if x1<=-1 or x1>=n or x2<=-1 or x2>=m:
        return False
    if graph[x1][x2] == 0:
        graph[x1][x2] = 1
        dfs(x1-1, x2)
        dfs(x1, x2-1)
        dfs(x1+1, x2)
        dfs(x1, x2+1)
        return True
    return False

print(graph)

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
