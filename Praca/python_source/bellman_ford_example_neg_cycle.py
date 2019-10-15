from described.bellman_ford import bellman_ford, \
    print_bellman_ford
from described.graph import Edge, Graph, Vertex

G = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"),
                    "c": Vertex("c"), "d": Vertex("d"),
                    "e": Vertex("e")},
          edges=[Edge("a", "c", 10), Edge("a", "b", 3), 
                Edge("b", "a", 2), Edge("c", "d", -9), 
                Edge("d", "e", 7), Edge("e", "a", 1),
                Edge("e", "c", -5)])

print_bellman_ford(G, "a", bellman_ford(G, "a"))