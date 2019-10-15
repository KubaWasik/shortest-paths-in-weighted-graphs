from described.bellman_ford import bellman_ford, \
    print_bellman_ford
from described.graph import Edge, Graph, Vertex

G = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"),
                    "c": Vertex("c"), "d": Vertex("d"),
                    "e": Vertex("e")},
          edges=[Edge("a", "b", 4), Edge("a", "c", 5),
                Edge("b", "a", -3), Edge("b", "c", -4),
                Edge("c", "d", 7), Edge("d", "b", 9),
                Edge("d", "e", 10), Edge("e", "b", 8)])

print_bellman_ford(G, "e", bellman_ford(G, "e"))

