# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

q = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0],
]
def Dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1]*length
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        i = 0
        for index, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[index]:
                if cost[index] > vertex+cost[start]:
                    cost[index] = vertex + cost[start]
                    parent[i] = start
            i += 1


        min_cost = float('inf')
        for index in range(length):
            if min_cost > cost[index] and not is_visited[index]:
                min_cost = cost[index]
                start = index

    return cost




# s = int (input('от какой вершины идти: '))
s=0
print(Dijkstra(q, s))