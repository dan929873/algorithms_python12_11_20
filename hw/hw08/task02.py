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
        for index, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[index]:
                if cost[index] > vertex+cost[start]:
                    cost[index] = vertex + cost[start]
                    parent[index] = start

        min_cost = float('inf')
        for index in range(length):
            if min_cost > cost[index] and not is_visited[index]:
                min_cost = cost[index]
                start = index

    my_list_parens = [[] for _ in range(length)]
    for i in range(length):
        if is_visited[i]:
            my_list_parens[i].append(i)
            j = i
            while parent[j] != -1:
                my_list_parens[i].append(parent[j])
                j = parent[j]

            my_list_parens[i].reverse()

    return cost, my_list_parens

s = int (input('от какой вершины идти: '))

cost, par = Dijkstra(q, s)
print(cost)
print(*par, sep='\n')
