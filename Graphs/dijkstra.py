from graph import Graph


def Dijkstra(G: Graph, src):
    n = G.get_vertices_number()
    adj_list = G.get_adjacent_list()

    path_to = [float('inf') for _ in range(n)]
    path_to[src] = 0

    is_gone = [False for _ in range(n)]

    for _ in range(n-1):

        # находим вершину с минимальным путём среди ещё не пройденных

        min_path = float('inf')
        u = -1
        for i in range(n):
            if not is_gone[i] and path_to[i] < min_path:
                min_path = path_to[i]
                u = i

        # и фиксируем её

        is_gone[u] = True

        for v in adj_list[u].items():
            new_path = path_to[u] + v[1]
            if path_to[v[0]] > new_path:
                path_to[v[0]] = new_path

    return path_to
