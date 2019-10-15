from copy import deepcopy
from math import inf


def faster_matrix_multiply(g):
    n = len(g.vertices)
    distance = deepcopy(g.distance_matrix)
    m = 1
    while n - 1 > m:
        old_distance = deepcopy(distance)
        for i in range(n):
            for j in range(n):
                distance[i][j] = inf
                for k in range(n):
                    distance[i][j] = \
                        min(distance[i][j], 
                            old_distance[i][k] 
                            + old_distance[k][j])
        m = 2 * m
    g.distance_matrix = deepcopy(distance)
    return distance
