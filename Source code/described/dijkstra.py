import heapq
from collections import deque
from math import inf

from described.graph import Graph, Vertex


def dijkstra(g: Graph, s: str):
    """
    Funkcja algorytmu Dijkstry

        :param g: Obiekt klasy Graph, graf na którym wykonujemy algorytm
        :type g: Graph
        :param s: wierzchołek startowy, znak lub zbiór znaków ('a', 'b', 'start', 'punkt 1', ...)
        :type s: str
        :return: Odległości od danego wierzchołka 's' do wszystkich pozostałych w grafie

    Zwracana jest krotka:
        (distance, path)
    zawierająca odległości od wierzchołka 's' oraz lista poprzedników
    oprócz zwracanego wyniku, algorytm zapisuje wyniki do obiektów wierzchołka w grafie (klasa Vertex)
    """
    # zamieniamy s jako zwykłą nazwę wierzchołka na obiekt klasy Vertex
    s: Vertex = g.vertices[s]
    # inicjujemy zbiory odległości oraz poprzedników wartościami domyślnymi (inf i None)
    s.distance = {}
    s.path = {}
    for v in g.vertices:
        s.distance[v] = inf
        s.path[v] = None
    s.distance[s.name] = 0
    # jeśli wierzchołek badany nie ma sąsiadów, bez sensu jest dalsze wykonywanie algorytmu,
    # więc zwracamy wartości domyślne
    if len(g.neighbors[s.name]) == 0:
        print("Wierzchołek '{}' nie posiada krawędzi wychodzących (może być wierzchołkiem izolowanym)".format(s.name))
        return s.distance, s.path
    # tworzymy kopię zbioru wierzchołków, będziemy z niej usuwać wierzchołki już odwiedzone
    nodes = [v for v in g.vertices]
    # tworzymy kolejkę priorytetową, umieszczamy na niej startowy wierzchołek i ustawiamy odległość (wagę) równą 0
    h = [(s.distance[s.name], s.name)]
    # wykonujemy aż się skończą wierzchołki lub kolejka będzie pusta
    while nodes and h:
        # pobieramy z kolejki pierwszy (co z własności kolejki priorytetowej idzie najbliższy) wierzchołek
        try:
            min_weight, nearest = heapq.heappop(h)
            # jeśli w kolejce znajduje się wierzchołek już przetworzony, pomijamy go i próbujemy ściągnąć taki, który
            # jeszcze się znajduje w zbiorze nie przetworzonych wierzchołków
            while nearest not in nodes:
                min_weight, nearest = heapq.heappop(h)
        # jeśli jednak nie ma już na kolejce takiego wierzchołka, oznacza to że pozostałe są nieosiągalne,
        # ustawiamy odległość na inf, poprzednik na None dla pozostałych wierzchołków i wychodzimy z pętli
        except IndexError:
            for node in nodes:
                s.distance[node] = inf
                s.path[node] = None
            break
        nodes.remove(nearest)
        # dla każdego wierzchołka sąsiedniego do najbliższego (nearest) wykonujemy relaksację
        for end, weight in [(x.end, x.weight) for x in g.edges if x.start == nearest]:
            w = min_weight + weight
            # jeśli dla badanego sąsiada droga jest krótsza, dodajemy go do kolejki
            if w < s.distance[end]:
                s.distance[end] = w
                s.path[end] = nearest
                heapq.heappush(h, (s.distance[end], end))
    # zwracamy krotkę zawierającą odległości oraz zbiór poprzedników
    return s.distance, s.path


def print_dijkstra(g: Graph, s: str):
    s: Vertex = g.vertices[s]
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


if __name__ == "__main__":
    print(dijkstra.__doc__)
