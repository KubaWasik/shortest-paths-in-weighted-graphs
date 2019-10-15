def floyd_warshall(g):
    n = len(g.vertices)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g.distance_matrix[i][j] \
                        > g.distance_matrix[i][k] \
                        + g.distance_matrix[k][j]:
                    g.distance_matrix[i][j] \
                        = g.distance_matrix[i][k] \
                          + g.distance_matrix[k][j]
                    g.path_matrix[i][j] \
                        = g.path_matrix[i][k]
    for vertex in g.vertices:
        g.vertices[vertex].distance = {
            v: g.distance_matrix[g.indexes[vertex]][
                g.indexes[v]] for v in g.vertices}
        g.vertices[vertex].path = {
            v: g.path_matrix[g.indexes[vertex]][
                g.indexes[v]] for v in g.vertices}
    return g.distance_matrix, g.path_matrix


if __name__ == "__main__":
    print("Plik zawierający funkcję algorytmu Floyda-Warshalla")
