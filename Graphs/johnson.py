from graph import Graph
from bellman_ford import Bellman_Ford
from dijkstra import Dijkstra


def Johnson(G: Graph):
    n = G.get_vertices_number()

    # изменяем веса на неотрицательные
    # 1) считаем значения функции h(u)

    G_1 = G.copy()
    new_vertex = G_1.add_vertex()
    for v in range(n):
        G_1.add_edge(new_vertex, v, 0)
    h = Bellman_Ford(G_1, new_vertex)

    # 2) w'(u-v) = w(u-v) + h(u) - h(v)
    G_2 = G.copy()
    for edge in G_2.edges:
        G_2.add_edge(edge[0], edge[1],
                     edge[2] + h[edge[0]] - h[edge[1]], True)

    # Применяем к получившемуся графу алгоритм Дейкстры
    shortest_paths = []
    for i in range(n):
        shortest_paths.append(Dijkstra(G_2, i))

    return shortest_paths
