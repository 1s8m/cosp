visited = [False] * 9
graph = [
    []
    , [2, 3, 8]
    , [1, 7]
    , [1, 4, 5]
    , [3, 5]
    , [3, 4]
    , [7]
    , [2, 6, 8]
    , [1, 7]
]

def dfs(graph, v, visited):
    visited[v] = True # 현재 위치는 방문 # 스택에 들어간 순서
    print(v, end=' ') # 방문한 위치는 바로 출력

    for i in graph[v]: # 현재 위치에 연결된 노드들을 다 돌아가면서 방문여부 체크
        if not visited[i]: # 각각의 노드에 방문한 적이 있었나? 없었다면 방문!
            dfs(graph, i, visited)

dfs(graph, 1, visited)

# DFS stack LIFO