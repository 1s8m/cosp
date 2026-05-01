import heapq

INF = int(1e9)

n, m = 6, 11
start_node = 1
# graph = [[] * (n+1)] # [[]] 이렇게만 정의됨
graph = [[] for _ in range(n+1)] 
# visited = [False] * (n+1)
distance = [INF] * (n+1)

graph[1].append([2, 2])
graph[1].append([3, 5])
graph[1].append([4, 1])
graph[2].append([3, 3])
graph[2].append([4, 2])
graph[3].append([2, 3])
graph[3].append([6, 5])
graph[4].append([3, 3])
graph[4].append([5, 1])
graph[5].append([3, 1])
graph[5].append([6, 2])


# def get_smallest_node():
#     min_value = INF
#     index = 0 # 거리가 가장 가까운 노드의 인덱스 초기 세팅
#     for i in range(1, n+1):
#         if not visited[i] and distance[i] < min_value : # 방문하지 않았고, 거리가 더 짧은 노드가 발견된다면,
#             index = i
#             min_value = distance[i]
#     return index # 호출 시점의 조건에 해당하는 노드의 index만 필요함.

def dijkstra(start):
    # visited[start] = True

    q = [] # heapq로 사용할 리스트 먼저 정의
    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # for d in graph[start]:
    #     distance[d[0]] = d[1] # distance 테이블 초회차 일괄 업데이트!
    ### 이 코드가 필요했던 건, distance가 가장 짧은 노드를 선택하기 위한 사전 작업..

    # for _ in range(n-1): # start 를 제외한 나머지 n-1 개 노드 횟수만큼 아래 반복
    while q:
        # now = get_smallest_node()
        # visited[now] = True
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue # now 노드를 이미 처리한 적이 있다면 (INF 와 비교라 등호 의미가 없을 듯..)

        # for d in graph[now]:
        for d in graph[now]:
            cost = distance[now] + d[1]
            if cost < distance[d[0]]:
                distance[d[0]] = cost
                heapq.heappush(q, (cost, d[0]))

dijkstra(start_node)

for each in range(1, n + 1):
    if distance[each] == INF:
        print("infinity")
    else:
        print(distance[each])