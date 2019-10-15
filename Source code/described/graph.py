from dataclasses import dataclass

from math import inf


@dataclass
class Edge:
    """
    Klasa krawędzi, jest to klasa z dekoratorem dataclass, stworzona tak by zachowywać
    się jak krotka (tuple) lecz będąca obiektem mutowalnym
    moduł dataclasses oraz dekorator dataclass wymaga Pythona w wersji 3.7+
    pola:
        start: str - wierzchołek początkowy krawędzi, traktowany jako znak (bądź zbiór znaków)
        end: str - wierzchołek końcowy krawędzi, tak samo jak powyżej
        weight: int - waga krawędzi, reprezentowana jako liczba zmiennoprzecinkowa (float)
    """
    start: str
    end: str
    weight: float


@dataclass
class Vertex:
    """
    Klasa wierzchołka, tak samo jak klasa Edge, jest z dekoratorem dataclass
    pola:
        name: str - nazwa wierzchołka, może to być jedna litera albo całe słowo
        distance: dict - pole dla wyników algorytmów - długości najkrótszych ścieżek, domyślnie puste,
                         wyniki przypisywane podczas wykonywania algorytmu
        path: dict - również wynik algorytmu, domyślnie pusty, zawiera poprzedniki z których buduje się ścieżki
    """
    name: str
    distance: dict = None
    path: dict = None


class Graph:
    """
    Klasa grafu, graf reprezentowany jako:
        - lista krawędzi (edges: list),
        - zbiór wierzchołków(vertices: dict),
        - lista sąsiedztwa (neighbors: dict),
        - macierzowa wersja reprezentacji będąca listą list (distance_matrix: list),
        - macierz poprzedników (path_matrix: list)
    Pojedyncza krawędź (edge) jest obiektem klasy Edge stworzonej z dekoratorem dataclass, a wierzchołek przez klasę
    Vertex
    """

    def __init__(self, vertices: dict, edges: list):
        """
        Konstruktor inicjuje wierzchołki (vertices), krawędzie(edges) oraz sąsiadów (neighbors)

            :param vertices: Lista wierzchołków reprezentowana jako słownik, klucz to nazwa, wartość to obiekt Vertex
            :type vertices: dict
            :param edges: Lista krawędzi (obiektów klasy Edge)
            :type edges: list

        """
        # inicjowane są zbiory wierzchołków, krawędzi oraz sąsiadów, tworzone są też macierzowe reprezentacje grafu
        # oraz macierz poprzedników
        self.vertices = vertices
        self.edges = edges
        # zmienna pomocnicza indexes to zbiór, który używany jest do przekształcenia nazwy wierzchołka w indeks
        # odpowiadający mu w macierzowej postaci grafu
        self.indexes = {}
        self.neighbors = {v: [(edge.end, edge.weight) for edge in self.edges if edge.start == v] for v in self.vertices}
        i: int = 0
        # żeby nie komplikować reprezentacji grafu, przyjmuję że wierzchołki będą posortowane alfabetycznie
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

    def __str__(self):
        out = "Graf o wierzchołkach: {}\nKrawędzie:\n".format([v for v in self.vertices])
        for edge in self.edges:
            out += "{0.start} -> {0.end} waga: {0.weight}\n".format(edge)
        return out

    def __repr__(self):
        out = "<Graph Class object - {} vertices, {} edges>".format(len(self.vertices), len(self.edges))
        return out


if __name__ == "__main__":
    print(Graph.__doc__)
