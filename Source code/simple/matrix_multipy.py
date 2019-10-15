from copy import deepcopy
from math import inf

from simple.bellman_ford import bellman_ford
from simple.graph import Graph


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

    g.distance_matrix = deepcopy(distance)

    return distance


def faster_matrix_multiply(g: Graph):
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

    m = 1
    while n - 1 > m:
        old_distance = deepcopy(distance)
        for i in range(n):
            for j in range(n):
                distance[i][j] = inf
                for k in range(n):
                    distance[i][j] = min(distance[i][j], old_distance[i][k] + old_distance[k][j])
        m = 2 * m

    g.distance_matrix = deepcopy(distance)

    return distance


if __name__ == "__main__":
    print("Plik zawierający funkcję algorytmu z iloczynem odległości oraz jego ulepszoną wersję")
