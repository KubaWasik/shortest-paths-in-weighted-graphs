import heapq
from collections import deque
from copy import deepcopy
from dataclasses import dataclass

from math import inf


@dataclass
class Vertex:
    name: str
    distance: dict = None
    path: dict = None


@dataclass
class Edge:
    start: str
    end: str
    weight: int


class Graph:
    def __init__(self, vertices: dict, edges: list):
        self.vertices = vertices
        self.edges = edges
        self.indexes = {}
        self.neighbors = {v: [(edge.end, edge.weight) for edge in self.edges if edge.start == v] for v in self.vertices}
        i: int = 0
        for v in sorted(self.vertices):
            self.indexes[v] = i
            i += 1
        n = len(self.vertices)
        self.distance_matrix = [[inf] * n for _ in range(n)]
        self.path_matrix = [[None] * n for _ in range(n)]
        for vertex in self.vertices:
            for neighbor, weight in self.neighbors[vertex]:
                self.distance_matrix[self.indexes[vertex]][self.indexes[neighbor]] = weight
                self.path_matrix[self.indexes[vertex]][self.indexes[neighbor]] = neighbor
        for i in range(n):
            self.distance_matrix[i][i] = 0

    def __str__(self):
        out = "Graf o wierzchołkach:\n\t{}\nKrawędzie:\n".format([v for v in self.vertices])
        if len(self.edges) == 0:
            out += "\tbrak krawędzi\n"
        else:
            for edge in self.edges:
                out += "\t{0.start} -> {0.end} waga: {0.weight}\n".format(edge)
        return out

    def __repr__(self):
        out = "<Graph Class object - {} vertices, {} edges>".format(len(self.vertices), len(self.edges))
        return out

    def dijkstra_naive(self, s: str = "a"):
        s: Vertex = self.vertices[s]
        s.distance = {}
        s.path = {}
        for v in self.vertices:
            s.distance[v] = inf
            s.path[v] = None
        s.distance[s.name] = 0

        if len(self.neighbors[s.name]) == 0:
            print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)"
                  .format(s.name))
            return s.distance, s.path

        nodes = [v for v in self.vertices]

        while nodes:
            nearest = min(nodes, key=lambda node: s.distance[node])
            nodes.remove(nearest)
            if s.distance[nearest] == inf:
                break
            for end, weight in [(x.end, x.weight) for x in self.edges if x.start == nearest]:
                w = s.distance[nearest] + weight
                if w < s.distance[end]:
                    s.distance[end] = w
                    s.path[end] = nearest

        return s.distance, s.path

    def dijkstra(self, s: str = "a"):
        s: Vertex = self.vertices[s]
        s.distance = {}
        s.path = {}
        for v in self.vertices:
            s.distance[v] = inf
            s.path[v] = None
        s.distance[s.name] = 0

        if len(self.neighbors[s.name]) == 0:
            print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)"
                  .format(s.name))
            return s.distance, s.path

        nodes = [v for v in self.vertices]
        h = [(s.distance[s.name], s.name)]
        while nodes and h:
            try:
                min_weight, nearest = heapq.heappop(h)
                while nearest not in nodes:
                    min_weight, nearest = heapq.heappop(h)
            except IndexError:
                for node in nodes:
                    s.distance[node] = inf
                    s.path[node] = None
                break
            nodes.remove(nearest)

            for end, weight in [(x.end, x.weight) for x in self.edges if x.start == nearest]:
                w = min_weight + weight
                if w < s.distance[end]:
                    s.distance[end] = w
                    s.path[end] = nearest
                    heapq.heappush(h, (s.distance[end], end))

        return s.distance, s.path

    def bellman_ford(self, s: str = "a"):
        s: Vertex = self.vertices[s]
        if len(self.neighbors[s.name]) == 0:
            return -2

        s.distance = {}
        s.path = {}
        for v in self.vertices:
            s.distance[v] = inf
            s.path[v] = None
        s.distance[s.name] = 0

        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                if s.distance[edge.start] != inf and s.distance[edge.start] + edge.weight < s.distance[edge.end]:
                    s.distance[edge.end] = s.distance[edge.start] + edge.weight
                    s.path[edge.end] = edge.start

        for edge in self.edges:
            if s.distance[edge.start] != inf and s.distance[edge.start] + edge.weight < s.distance[edge.end]:
                return -1

        return s.distance, s.path

    def bellman_ford_no_check(self, s: str = "a"):
        s: Vertex = self.vertices[s]
        s.distance = {}
        s.path = {}
        for v in self.vertices:
            s.distance[v] = inf
            s.path[v] = None
        s.distance[s.name] = 0

        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                if s.distance[edge.start] != inf and s.distance[edge.start] + edge.weight < s.distance[edge.end]:
                    s.distance[edge.end] = s.distance[edge.start] + edge.weight
                    s.path[edge.end] = edge.start

        return s.distance, s.path

    def dijkstra_all_vertices(self):
        distances = {}
        path = {}
        for vertex in self.vertices:
            distances[vertex], path[vertex] = self.dijkstra(vertex)
        return distances, path

    def matrix_multiply(self):
        for vertex in self.vertices:
            code = self.bellman_ford(vertex)
            if code == -1:
                print("Ujemny cykl")
                return False
            elif code == -2:
                continue
            else:
                break

        n = len(self.vertices)
        distance = deepcopy(self.distance_matrix)

        for _ in range(n - 2):
            old_distance = deepcopy(distance)
            for i in range(n):
                for j in range(n):
                    distance[i][j] = inf
                    for k in range(n):
                        distance[i][j] = min(distance[i][j], old_distance[i][k] + self.distance_matrix[k][j])
        return distance

    def faster_matrix_multiply(self):
        for vertex in self.vertices:
            code = self.bellman_ford(vertex)
            if code == -1:
                print("Ujemny cykl")
                return False
            elif code == -2:
                continue
            else:
                break

        n = len(self.vertices)
        distance = deepcopy(self.distance_matrix)

        m = 1
        while n - 1 > m:
            old_distance = deepcopy(distance)
            for i in range(n):
                for j in range(n):
                    distance[i][j] = inf
                    for k in range(n):
                        distance[i][j] = min(distance[i][j], old_distance[i][k] + old_distance[k][j])
            m = 2 * m

        return distance

    def floyd_warshall(self):
        for vertex in self.vertices:
            code = self.bellman_ford(vertex)
            if code == -1:
                print("Ujemny cykl")
                return False
            elif code == -2:
                continue
            else:
                break

        n = len(self.vertices)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.distance_matrix[i][j] > self.distance_matrix[i][k] + self.distance_matrix[k][j]:
                        self.distance_matrix[i][j] = self.distance_matrix[i][k] + self.distance_matrix[k][j]
                        self.path_matrix[i][j] = self.path_matrix[i][k]

        for vertex in self.vertices:
            self.vertices[vertex].distance = {v: self.distance_matrix[self.indexes[vertex]][self.indexes[v]]
                                              for v in self.vertices}
            self.vertices[vertex].path = {v: self.path_matrix[self.indexes[vertex]][self.indexes[v]]
                                          for v in self.vertices}

        return self.distance_matrix, self.path_matrix

    def johnson(self):
        for vertex in self.vertices:
            code = self.bellman_ford(vertex)
            if code == -1:
                print("Ujemny cykl")
                return False
            elif code == -2:
                continue
            else:
                break

        self.vertices["-s"] = Vertex("-s")
        self.neighbors["-s"] = []
        for vertex in self.vertices:
            self.edges.append(Edge("-s", vertex, 0))
            self.neighbors["-s"] += [(vertex, 0)]
        result = self.bellman_ford("-s")
        if not result:
            return False
        distances_b_f, _ = result
        for edge in self.edges:
            edge.weight = edge.weight + distances_b_f[edge.start] - distances_b_f[edge.end]
        s_edges = [edge for edge in self.edges if edge.start == "-s"]
        for edge in s_edges:
            self.edges.remove(edge)
        self.vertices.pop("-s")
        self.neighbors.pop("-s")
        distances = {}
        path = {}
        for vertex in self.vertices:
            distances[vertex], path[vertex] = self.dijkstra(vertex)
        for v_1 in self.vertices:
            for v_2 in self.vertices:
                distances[v_1][v_2] += distances_b_f[v_2] - distances_b_f[v_1]
        for edge in self.edges:
            edge.weight = edge.weight + distances_b_f[edge.start] - distances_b_f[edge.end]
        return distances, path

    def print_dijkstra(self, s: str):
        s: Vertex = self.vertices[s]
        for v in s.distance:
            if s.path[v]:
                print('Droga z {} do {} (odległość: {}): '.format(s.name, v, s.distance[v]), end='')
                p: str = v
                que = deque()
                while s.path[p]:
                    que.append(p)
                    p = s.path[p]
                que.append(s.name)
                while que:
                    vertex = que.pop()
                    if vertex == v:
                        print('{}\n'.format(v), end='')
                        continue
                    print('{} -> '.format(vertex), end='')

    def print_bellman_ford(self, s: str, result):
        if result == -1:
            print("Ujemny cykl")
            return
        elif result == -2:
            print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)".format(s))
            return
        s: Vertex = self.vertices[s]
        for v in s.distance:
            if s.path[v]:
                print('Droga z {} do {} (odległość: {}): '.format(s.name, v, s.distance[v]), end='')
                p: str = v
                que = deque()
                while s.path[p]:
                    que.append(p)
                    p = s.path[p]
                que.append(s.name)
                while que:
                    vertex = que.pop()
                    if vertex == v:
                        print('{}\n'.format(v), end='')
                        continue
                    print('{} -> '.format(vertex), end='')

    def print_floyd_warshall(self, result):
        if not result:
            return
        distance, path = result
        for u in self.vertices:
            for v in self.vertices:
                if path[self.indexes[u]][self.indexes[v]]:
                    print('Droga z {} do {} (odległość: {}): '
                          .format(u, v,
                                  distance[self.indexes[u]][self.indexes[v]]), end='')
                    p: str = u
                    while path[self.indexes[p]][self.indexes[v]]:
                        print('{} -> '.format(p), end='')
                        p = path[self.indexes[p]][self.indexes[v]]
                    print('{}\n'.format(v), end='')

    def print_johnson(self, result):
        if not result:
            return
        distance, path = result
        for u in self.vertices:
            for v in self.vertices:
                if path[u][v]:
                    print('Droga z {} do {} (odległość: {}): '
                          .format(u, v,
                                  distance[u][v]), end='')
                    p: str = v
                    que = deque()
                    while path[u][p]:
                        que.append(p)
                        p = path[u][p]
                    que.append(u)
                    while que:
                        vertex = que.pop()
                        if vertex == v:
                            print('{}\n'.format(v), end='')
                            continue
                        print('{} -> '.format(vertex), end='')


if __name__ == "__main__":
    print("\nPlik z klasą Graph zawierającą implementację grafu, wszystkich algorytmów oraz funkcji pomocniczych\n"
          "do wypisywania grafu oraz wyniku algorytmów.\n")
