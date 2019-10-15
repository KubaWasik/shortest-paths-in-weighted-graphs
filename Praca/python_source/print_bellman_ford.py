def print_bellman_ford(g: Graph, s: str, result):
    if result == -1:
        print("Ujemny cykl")
        return
    elif result == -2:
        print("Wierzchołek '{}' nie posiada krawędzi \
               wychodzących (może być wierzchołkiem \
               izolowanym)".format(s))
        return
    s: Vertex = g.vertices[s]
    for v in s.distance:
        if s.path[v]:
            print('Droga z {} do {} (odległość: {}): '
                  .format(s.name, v, s.distance[v]), 
                          end='')
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