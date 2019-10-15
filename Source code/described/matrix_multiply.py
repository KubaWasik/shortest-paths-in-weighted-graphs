from copy import deepcopy

from math import inf

from described.bellman_ford import bellman_ford
from described.graph import Graph


def matrix_multiply(g: Graph):
    for vertex in g.vertices:
        code = bellman_ford(g, vertex)
        if code == -1:
            print("Ujemny cykl")
            return False
        elif code == -2:
            continue
        else:
            break

    n = len(g.vertices)
    distance = deepcopy(g.distance_matrix)

    for _ in range(n - 2):
        old_distance = deepcopy(distance)
        for i in range(n):
            for j in range(n):
                distance[i][j] = inf
                for k in range(n):
                    distance[i][j] = min(distance[i][j], old_distance[i][k] + g.distance_matrix[k][j])

    # wyniki przypisujemy do grafu
    g.distance_matrix = deepcopy(distance)

    return distance


def faster_matrix_multiply(g: Graph):
    """
    Funkcja algorytmu z iloczynem odległości - wersja ulepszona
        :param g: Obiekt klasy Graph, graf na którym wykonujemy algorytm
        :type g: Graph
        :return: Najkrótsze ścieżki między wszystkimi wierzchołkami w postaci macierzy

    Zwracana jest macierz z odległościami, macierz jest listą list
    oprócz zwracania wyników, algorytm przypisuje wyniki do obiektu macierzy w grafie (distance_matrix)
    """
    # dodatkowe sprawdzanie czy graf nie zawiera ujemnego cyklu
    for vertex in g.vertices:
        code = bellman_ford(g, vertex)
        if code == -1:
            print("Ujemny cykl")
            return False
        elif code == -2:
            continue
        else:
            break

    # wyznaczamy n - wielkość macierzy
    n = len(g.vertices)
    # wykonujemy tak zwaną głęboką kopię bazowego grafu
    distance = deepcopy(g.distance_matrix)

    # wykonujemy główne działanie algorytmu log(V) razy
    m = 1
    while n - 1 > m:
        # działamy na macierzy distance ale potrzebować będziemy starych wartości więc tworzymy kopię
        old_distance = deepcopy(distance)
        for i in range(n):
            for j in range(n):
                distance[i][j] = inf
                for k in range(n):
                    distance[i][j] = min(distance[i][j], old_distance[i][k] + old_distance[k][j])
        m = 2 * m

    # wyniki przypisujemy do grafu
    g.distance_matrix = deepcopy(distance)

    return distance


if __name__ == "__main__":
    print(faster_matrix_multiply.__doc__)
