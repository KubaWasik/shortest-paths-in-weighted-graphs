from collections import deque
from math import inf

from described.graph import Graph, Vertex


def bellman_ford(g: Graph, s: str):
    """
    Funkcja algorytmu Bellmana-Forda

        :param g: Obiekt klasy Graph, badany graf
        :type g: Graph
        :param s: wierzchołek startowy, znak lub zbiór znaków ('a', 'b', 'start', 'punkt 1', ...)
        :type s: str
        :return: Odległości od danego wierzchołka 's' do wszystkich pozostałych w grafie

    Zwracana jest krotka:
        (distance, path)
    czyli odległości od wierzchołka 's' oraz lista poprzedników
    oprócz zwracania wyników, algorytm zapisuje wyniki w obiekcie wierzchołka grafu (klasa Vertex)
    """
    # zamieniamy s jako zwykłą nazwę wierzchołka na obiekt klasy Vertex
    s: Vertex = g.vertices[s]
    # jeśli wierzchołek nie ma sąsiadów to zwracamy -2, na potrzeby sprawdzania dla algorytmów Floyda-Warshalla
    # i Johnsona
    if len(g.neighbors[s.name]) == 0:
        print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)"
              .format(s.name))
        return -2
    # inicjujemy zbiory odległości oraz poprzedników wartościami domyślnymi (inf i None)
    s.distance = {}
    s.path = {}
    for v in g.vertices:
        s.distance[v] = inf
        s.path[v] = None
    s.distance[s.name] = 0
    # wykonujemy relaksację dla wszystkich krawędzi n - 1 razy, gdzie n to liczba wierzchołków w grafie
    for _ in range(len(g.vertices) - 1):
        for edge in g.edges:
            if s.distance[edge.start] != inf and s.distance[edge.start] + edge.weight < s.distance[edge.end]:
                s.distance[edge.end] = s.distance[edge.start] + edge.weight
                s.path[edge.end] = edge.start
    # sprawdzamy czy występuje ujemny cykl, jeśli tak to zwracamy -1, również na potrzeby sprawdzania
    # dla innych algorytmów
    for edge in g.edges:
        if s.distance[edge.start] != inf and s.distance[edge.start] + edge.weight < s.distance[edge.end]:
            return -1
    # zwracamy krotkę zawierającą odległości oraz zbiór poprzedników
    return s.distance, s.path


def print_bellman_ford(g: Graph, s: str, result):
    if result == -1:
        print("Ujemny cykl")
        return
    elif result == -2:
        print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)".format(s))
        return
    s: Vertex = g.vertices[s]
    for v in s.distance:
        if s.path[v]:
            print('Droga z {} do {} (odległość: {}): '
                  .format(s.name, v, s.distance[v]), end='')
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


if __name__ == "__main__":
    print(bellman_ford.__doc__)
