def print_johnson(g, result):
    if not result:
        return
    distance, path = result
    for u in g.vertices:
        for v in g.vertices:
            if path[u][v]:
                print('Droga z {} do {} (odległość: \
                    {}): '.format(u, v,
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
                   print('{}->'.format(vertex), end='')