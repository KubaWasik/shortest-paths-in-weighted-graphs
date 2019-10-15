from collections import deque

from described.bellman_ford import bellman_ford
from described.dijkstra import dijkstra
from described.graph import Edge, Graph, Vertex


def johnson(g: Graph):
    """
    Funkcja algorytmu Johnsona

        :param g: Obiekt klasy Graph, graf na którym wykonujemy algorytm
        :type g: Graph
        :return: Najkrótsze ścieżki między wszystkimi wierzchołkami oraz listę poprzedników

    Zwracana jest krotka:
        (distances, path)
    zawierająca odległości między wszystkimi wierzchołkami oraz macierz poprzedników
    oprócz zwracania wyników, algorytm przypisuje wyniki do obiektów wierzchołków grafu (klasa Vertex)
    """

    # sprawdzanie na wstępie czy graf zawiera ujemny cykl, nadmiarowe - usunięcie przyśpieszy w pewnym stopniu algorytm
    # przechodzimy przez wszystkie wierzchołki dlatego, że dla wierzchołka izolowanego lub takiego, który nie ma
    # krawędzi wychodzących algorytm bellmana_forda nie zwróci False, tylko dla każdego wierzchołka odległość będzie inf
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

    # tworzymy pomocniczy wierzchołek "-s" oraz krawędzie z wierzchołka "-s" do każdego innego w grafie
    g.vertices["-s"] = Vertex("-s")
    g.neighbors["-s"] = []
    for vertex in g.vertices:
        g.edges.append(Edge("-s", vertex, 0))
        g.neighbors["-s"] += [(vertex, 0)]

    # po utworzeniu wierzchołka "-s" obliczamy odległości z wierzchołka "-s" do pozostałych wierzchołków
    # dodatkowo sprawdzamy czy graf nie zawiera ujemnych cykli, jeśli tak to wychodzimy z funkcji
    result = bellman_ford(g, "-s")
    # jeśli algorytm Bellmana-Forda zwróci False, również algorytm Johnsona zwraca False - ujemny cykl
    if not result:
        return False
    distances_b_f, _ = result
    # zmieniamy wagi dla każdej krawędzi uwzględniając odległości wyliczone przez algorytm Bellmana-Forda
    # przez co likwidujemy ujemne wagi i umożliwiamy użycie algorytmu Dijkstry
    for edge in g.edges:
        edge.weight = edge.weight + distances_b_f[edge.start] - distances_b_f[edge.end]
    # usuwamy wierzchołek "-s" oraz wszystkie krawędzie wyprowadzone z tego wierzchołka
    s_edges = [edge for edge in g.edges if edge.start == "-s"]
    for edge in s_edges:
        g.edges.remove(edge)
    g.vertices.pop("-s")
    g.neighbors.pop("-s")
    # wyliczamy algorytmem Dijkstry odległości i poprzedniki dla każdego wierzchołka
    distances = {}
    path = {}
    for vertex in g.vertices:
        distances[vertex], path[vertex] = dijkstra(g, vertex)
    # ponownie zmieniamy wagi dla każdej krawędzi oraz poprawiamy odległości uwzględniając poprzednio zmienione
    # ujemne wagi
    for v_1 in g.vertices:
        for v_2 in g.vertices:
            distances[v_1][v_2] += distances_b_f[v_2] - distances_b_f[v_1]
    for edge in g.edges:
        edge.weight = edge.weight + distances_b_f[edge.start] - distances_b_f[edge.end]

    # zwracamy krotkę zawierającą odległości oraz macierz poprzedników
    return distances, path


def print_johnson(g, result):
    if not result:
        return
    distance, path = result
    for u in g.vertices:
        for v in g.vertices:
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
    print(johnson.__doc__)
