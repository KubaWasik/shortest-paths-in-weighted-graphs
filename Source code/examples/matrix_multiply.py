from described.graph import Edge, Graph, Vertex
from described.matrix_multiply\
    import faster_matrix_multiply

G = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"),
                    "c": Vertex("c"), "d": Vertex("d"),
                    "e": Vertex("e")},
          edges=[Edge("a", "c", -3), Edge("a", "d", 2),
                 Edge("b", "a", -5), Edge("b", "c", 4),
                 Edge("c", "d", 6), Edge("d", "e", 1),
                 Edge("e", "b", 9), Edge("e", "c", -4)])

for line in faster_matrix_multiply(G):
    print(line)
