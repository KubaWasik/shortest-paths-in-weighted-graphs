def print_dijkstra(g: Graph, s: str):
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