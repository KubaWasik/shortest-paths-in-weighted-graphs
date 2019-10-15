from described.dijkstra import dijkstra, print_dijkstra
from described.graph import Edge, Graph, Vertex

G = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"),
                    "c": Vertex("c"), "d": Vertex("d"),
                    "e": Vertex("e"), "f": Vertex("f")},
          edges=[Edge("a", "b", 7), Edge("a", "c", 9),
                 Edge("a", "f", 14), Edge("b", "c", 10),
                 Edge("b", "d", 15), Edge("c", "d", 11),
                 Edge("c", "f", 2), Edge("d", "e", 6),
                 Edge("e", "f", 9)])

dijkstra(G, "a")
print_dijkstra(G, "a")
