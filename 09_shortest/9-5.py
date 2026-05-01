import heapq

n, m, c = 3, 2, 1
# INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [1001] * (n + 1)
# visited

graph[1].append((2, 4))
graph[1].append((3, 2))


def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue # now 노드를 이미 처리한 적이 있다면

        for each in graph[now]:
            cost = distance[now] + each[1]
            # print(each)
            if cost < distance[each[0]]:
                distance[each[0]] = cost
                heapq.heappush(q, (cost, each[0]))

dijkstra(c)
print(distance)

count = 0
max_distance = 0
for d in distance:
    if d != 1001:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)


