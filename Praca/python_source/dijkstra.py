import heapq
from math import inf


def dijkstra(g, s):
    s = g.vertices[s]
    s.distance = {}
    s.path = {}
    for v in g.vertices:
        s.distance[v] = inf
        s.path[v] = None
    s.distance[s.name] = 0
    nodes = [v for v in g.vertices]
    h = [(s.distance[s.name], s.name)]
    while nodes and h:
        try:
            min_weight, nearest = heapq.heappop(h)
            while nearest not in nodes:
                min_weight, nearest = heapq.heappop(h)
        except IndexError:
            for node in nodes:
                s.distance[node] = inf
                s.path[node] = None
            break
        nodes.remove(nearest)
        for end, weight in [(x.end, x.weight) for x in 
                        g.edges if x.start == nearest]:
            w = min_weight + weight
            if w < s.distance[end]:
                s.distance[end] = w
                s.path[end] = nearest
                heapq.heappush(h,(s.distance[end],end))
    return s.distance, s.path
