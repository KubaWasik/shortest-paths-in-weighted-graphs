from described.bellman_ford import bellman_ford
from described.graph import Graph


def floyd_warshall(g: Graph):
    """
    Funkcja algorytmu Floyda-Warshalla

        :param g: Obiekt klasy Graph, badany graf
        :type g: Graph
        :return: Najkrótsze ścieżki między wszystkimi wierzchołkami oraz listę poprzedników

    Zwracana jest krotka:
        (distances, path)
    zawierająca macierz odległości między wszystkimi wierzchołkami oraz macierz poprzedników
    oprócz zwracania wyników, algorytm zapisuje wyniki do obiektów wierzchołków w grafie (klasa Vertex)
    """

    # sprawdzamy czy podany graf nie zawiera ujemnych cykli, przechodzimy przez wszystkie wierzchołki dlatego,
    # że dla wierzchołka izolowanego lub takiego, który nie ma krawędzi wychodzących algorytm bellmana_forda
    # nie zwróci False, tylko dla każdego wierzchołka odległość będzie inf
    for vertex in g.vertices:
        # code może być wartością kodu błędu (-1 lub -2) lub też poprawnym wynikiem algorytmu
        code = bellman_ford(g, vertex)
        # -1 oznacza ujemny cykl wtedy wychodzimy z funkcji
        if code == -1:
            print("Ujemny cykl")
            return False
        # -2 oznacza że wierzchołek nie zawiera krawędzi wychodzących więc nie można stwierdzić czy występuje
        # ujemny cykl, więc przechodzimy do następnego
        elif code == -2:
            continue
        # jeśli nie nastąpił żaden błąd to graf nie zawiera ujemnych cykli - można przejść do algorytmu
        else:
            break
    # wyznaczamy wielkość macierzy
    n = len(g.vertices)
    # główna pętla algorytmu
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g.distance_matrix[i][j] > g.distance_matrix[i][k] + g.distance_matrix[k][j]:
                    g.distance_matrix[i][j] = g.distance_matrix[i][k] + g.distance_matrix[k][j]
                    g.path_matrix[i][j] = g.path_matrix[i][k]

    # przypisujemy wyniki do grafu
    for vertex in g.vertices:
        g.vertices[vertex].distance = {v: g.distance_matrix[g.indexes[vertex]][g.indexes[v]] for v in g.vertices}
        g.vertices[vertex].path = {v: g.path_matrix[g.indexes[vertex]][g.indexes[v]] for v in g.vertices}

    # zwracamy krotkę zawierającą macierz z odległościami oraz macierz poprzedników
    return g.distance_matrix, g.path_matrix


def print_floyd_warshall(g, result):
    if not result:
        return
    distance, path = result
    for u in g.vertices:
        for v in g.vertices:
            if path[g.indexes[u]][g.indexes[v]]:
                print('Droga z {} do {} (odległość: {}): '
                      .format(u, v,
                              distance[g.indexes[u]][g.indexes[v]]), end='')
                p: str = u
                while path[g.indexes[p]][g.indexes[v]]:
                    print('{} -> '.format(p), end='')
                    p = path[g.indexes[p]][g.indexes[v]]
                print('{}\n'.format(v), end='')


if __name__ == "__main__":
    print(floyd_warshall.__doc__)
