from graph import Graph


def Bellman_Ford(G: Graph, v) -> list:

    n = G.get_vertices_number()
    edges = G.get_edges()

    h = [float('inf') for _ in range(n)]
    h[v] = 0

    for _ in range(n):
        for edge in edges:
            new_path = h[edge[0]]+edge[2]
            if new_path <= h[edge[1]]:
                h[edge[1]] = new_path

    # проверка на цикл отрицательного веса
    for edge in edges:
        if h[edge[0]]+edge[2] < h[edge[1]]:
            return []

    return h
