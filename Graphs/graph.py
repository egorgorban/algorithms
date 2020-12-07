from random import randint as rint


class Graph():

    def __init__(self, is_empty=True, v_n=-1, e_n=-1):
        if not is_empty:
            if not v_n > 0:
                v_n = rint(5, 10)
            if not e_n > 0:
                e_n = rint(int(v_n*(v_n-1)/6), int(v_n*(v_n-1)/2))

            _adjacent_list = [{i: 0} for i in range(v_n)]
            for _ in range(e_n):
                u = rint(0, v_n-1)
                v = rint(0, v_n-1)
                while v == u or v in _adjacent_list[u]:
                    u = rint(0, v_n-1)
                    v = rint(0, v_n-1)
                is_negative = rint(1, 10) // 11
                if is_negative:
                    (_adjacent_list[u])[v] = rint(-10, -1)  # вес ребра
                else:
                    (_adjacent_list[u])[v] = rint(0, 100)  # вес ребра

            self.vertices_number = v_n
            self.edges_number = e_n
            self.edges, self.adjacent_matrix = self._make_matrix_from_list(
                _adjacent_list, True)
            self.adjacent_list = _adjacent_list
        else:
            self.vertices_number = 0
            self.edges_number = 0
            self.edges = []
            self.adjacent_list = []
            self.adjacent_matrix = []

    def _make_matrix_from_list(self, l: list, edges=False) -> list:
        n = len(l)
        m = [[float('inf')] * n for i in range(n)]
        if edges:
            e = []
        for i in range(n):
            dicts = l[i]
            for d in dicts.items():
                if edges and i != d[0]:
                    e.append((i, d[0], d[1]))
                m[i][d[0]] = d[1]
        if edges:
            return e, m
        return m

    def get_vertices_number(self):
        return self.vertices_number

    def get_edges_number(self):
        return self.edges_number

    def add_vertex(self) -> int:
        '''
        Добавляет вершину, 
        Возвращает её индекс в графе
        '''
        self.adjacent_list.append({self.vertices_number: 0})
        self.adjacent_matrix = self._make_matrix_from_list(self.adjacent_list)
        self.vertices_number += 1
        return self.vertices_number - 1

    def add_edge(self, u, v, w, is_change=False) -> bool:
        if not is_change:
            if v in self.adjacent_list[u]:
                return False
            self.edges_number += 1
        else:
            cur_w = self.adjacent_matrix[u][v]
            self.edges.remove((u, v, cur_w))
        self.edges.append((u, v, w))
        self.adjacent_list[u][v] = w
        self.adjacent_matrix[u][v] = w

    def get_edges(self):
        return self.edges[:]

    def get_adjacent_list(self):
        return self.adjacent_list[:]

    def get_adjacent_matrix(self):
        return self.adjacent_matrix[:]

    def show(self):
        print('Graph:\n[')
        for line in self.adjacent_matrix:
            print('\t', line, ',')
        print(']')
