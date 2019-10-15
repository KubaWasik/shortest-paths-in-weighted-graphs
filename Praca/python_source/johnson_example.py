from described.graph import Edge, Graph, Vertex
from described.johnson import johnson, print_johnson

G = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"),
                    "c": Vertex("c"), "d": Vertex("d"),
                    "e": Vertex("e")},
          edges=[Edge("a", "b", -1), Edge("a", "d", 8),
                 Edge("a", "e", 1), Edge("b", "c", -3),
                 Edge("b", "e", -4), Edge("c", "a", 9),
                 Edge("c", "e", 2), Edge("d", "c", -6),
                 Edge("e", "d", 7)])

print_johnson(G, johnson(G))