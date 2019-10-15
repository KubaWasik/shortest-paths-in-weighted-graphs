def print_floyd_warshall(g, result):
    if not result:
        return
    distance, path = result
    for u in g.vertices:
        for v in g.vertices:
            if path[g.indexes[u]][g.indexes[v]]:
                print('Droga z {} do {} (odległość: \
                      {}): '.format(u, v, distance[
                          g.indexes[u]][g.indexes[v]]), 
                          end='')
               p: str = u
               while path[g.indexes[p]][g.indexes[v]]:
                   print('{} -> '.format(p), end='')
                   p = path[g.indexes[p]][g.indexes[v]]
               print('{}\n'.format(v), end='')