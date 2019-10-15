from described.bellman_ford import bellman_ford
from described.dijkstra import dijkstra
from described.graph import Graph, Edge, Vertex


def johnson(g: Graph):
    g.vertices["s"] = Vertex("s")
    g.neighbors["s"] = []
    for vertex in g.vertices:
        g.edges.append(Edge("s", vertex, 0))
        g.neighbors["s"] += [(vertex, 0)]
    bf = bellman_ford(g, "s")
    if not bf:
        print("Ujemny cykl")
        return
    distances_b_f, _ = bf
    for edge in g.edges:
        edge.weight = edge.weight + \
                      distances_b_f[edge.start] \
                      - distances_b_f[edge.end]
    s_edges = [edge for edge in g.edges
               if edge.start == "s"]
    for edge in s_edges:
        g.edges.remove(edge)
    g.vertices.pop("s")
    g.neighbors.pop("s")
    distances = {}
    path = {}
    for vertex in g.vertices:
        distances[vertex], path[vertex] = \
            dijkstra(g, vertex)
    for v_1 in g.vertices:
        for v_2 in g.vertices:
            distances[v_1][v_2] += \
                distances_b_f[v_2] - distances_b_f[v_1]
    for edge in g.edges:
        edge.weight = edge.weight + \
                      distances_b_f[edge.start] \
                      - distances_b_f[edge.end]
    return distances, path
