from dataclasses import dataclass
from math import inf


@dataclass
class Edge:
    start: str
    end: str
    weight: int


@dataclass
class Vertex:
    name: str
    distance: dict = None
    path: dict = None


class Graph:
    def __init__(self, vertices: dict, edges: list):
        self.vertices = vertices
        self.edges = edges
        self.indexes = {}
        self.neighbors = {v: [(edge.end, edge.weight)
                              for edge in self.edges
                              if edge.start == v]
                          for v in self.vertices}
        for v in sorted(self.vertices):
            self.indexes[v] = i
            i += 1
        n = len(self.vertices)
        self.distance_matrix = [
            [inf] * n for _ in range(n)]
        self.path_matrix = [
            [None] * n for _ in range(n)]
        for vertex in self.vertices:
            for neighbor, weight \
                    in self.neighbors[vertex]:
                self.distance_matrix[
                    self.indexes[vertex]][
                    self.indexes[neighbor]] = weight
                self.path_matrix[
                    self.indexes[vertex]][
                    self.indexes[neighbor]] = neighbor
        for j in range(n):
            self.distance_matrix[j][j] = 0
