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

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 세팅
    visited[start] = True # 현재 출발점에 방문 처리
    while queue: # 큐가 있다면 알고리즘이 계속 돌아감
        v = queue.popleft()
        print(v, end=' ') # 큐에서 나오면 방문 -> 출력

        for i in graph[v]:
            if not visited[i]: # 방문한 적이 없으면 후보들을 큐에 넣어둠.
                queue.append(i)
                visited[i] = True 


bfs(graph, 1, visited)
# BFS queue FIFO