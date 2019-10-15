from math import inf


def bellman_ford(g, s):
    s = g.vertices[s]
    s.distance = {}
    s.path = {}
    for v in g.vertices:
        s.distance[v] = inf
        s.path[v] = None
    s.distance[s.name] = 0
    for _ in range(len(g.vertices) - 1):
        for edge in g.edges:
            if s.distance[edge.start] != inf and \
                    s.distance[edge.start] + \
                    edge.weight < s.distance[edge.end]:
                s.distance[edge.end] = \
                   s.distance[edge.start] + edge.weight
                s.path[edge.end] = edge.start
    for edge in g.edges:
        if s.distance[edge.start] != inf and \
                s.distance[edge.start] + edge.weight \
                < s.distance[edge.end]:
            return False
    return s.distance, s.path
