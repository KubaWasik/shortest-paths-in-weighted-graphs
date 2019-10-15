from described.all_in_one_class import Graph, Vertex, Edge

G1 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e"),
                     "f": Vertex("f")},
           edges=[Edge("a", "b", 7), Edge("a", "c", 9), Edge("a", "f", 14), Edge("b", "c", 10), Edge("b", "d", 15),
                  Edge("c", "d", 11), Edge("c", "f", 2), Edge("d", "e", 6), Edge("e", "f", 9)])

G2 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e")},
           edges=[Edge("a", "b", 4), Edge("a", "c", 5), Edge("b", "a", -3), Edge("b", "c", -4), Edge("c", "d", 7),
                  Edge("d", "b", 9), Edge("d", "e", 10), Edge("e", "b", 8)])

G3 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e"),
                     "f": Vertex("f"), "g": Vertex("g"), "h": Vertex("h")},
           edges=[Edge("b", "c", 9), Edge("b", "e", -1), Edge("b", "f", -10), Edge("c", "d", -8), Edge("d", "b", 7),
                  Edge("e", "b", 2), Edge("f", "b", 10), Edge("f", "g", -5), Edge("g", "h", -3)])

G4 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e"),
                     "f": Vertex("f")},
           edges=[Edge("a", "b", 2), Edge("a", "c", 10), Edge("b", "d", 20), Edge("c", "d", 1), Edge("c", "e", 1),
                  Edge("d", "f", 5), Edge("e", "f", 2)])

G5 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e"),
                     "f": Vertex("f"), "g": Vertex("g"), "h": Vertex("h"), "i": Vertex("i")},
           edges=[Edge("a", "c", 1), Edge("b", "a", 3), Edge("c", "b", 2), Edge("d", "g", -5), Edge("e", "d", 4),
                  Edge("f", "h", 8), Edge("g", "e", 10), Edge("g", "f", 2), Edge("h", "f", -1)])

G6 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e"),
                     "f": Vertex("f"), "g": Vertex("g"), "h": Vertex("h"), "i": Vertex("i")},
           edges=[])

G7 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e")},
           edges=[Edge("a", "c", -3), Edge("a", "d", 2), Edge("b", "a", -5), Edge("b", "c", 4), Edge("c", "d", 6),
                  Edge("d", "e", 1), Edge("e", "b", 9), Edge("e", "c", -4)])

G8 = Graph(vertices={"a": Vertex("a"), "b": Vertex("b"), "c": Vertex("c"), "d": Vertex("d"), "e": Vertex("e")},
           edges=[Edge("a", "b", -1), Edge("a", "d", 8), Edge("a", "e", 1), Edge("b", "c", -3), Edge("b", "e", -4),
                  Edge("c", "a", 9), Edge("c", "e", 2), Edge("d", "c", -6), Edge("e", "d", 7)])

# change number of graph here
G: Graph = G1

print('*' * 50)
print("Wyniki dla grafu:\n{}".format(G))
print("\nAlgorytm Dijkstry\n")
G.dijkstra("a")
G.print_dijkstra("a")
print()
print('-' * 50)
print("\nAlgorytm Bellmana-Forda\n")
G.print_bellman_ford("a", G.bellman_ford("a"))
print()
print('-' * 50)
print("\nAlgorytm wykorzystujący mnożenie macierzy\n\n\tWersja podstawowa\n")
for x in G.matrix_multiply():
    print(x)
print("\n\tWersja przyśpieszona\n")
for x in G.faster_matrix_multiply():
    print(x)
print()
print('-' * 50)
print("\nAlgorytm Floyda-Warshalla\n")
G.print_floyd_warshall(G.floyd_warshall())
print()
print('-' * 50)
print("\nAlgorytm Johnsona\n")
G.print_johnson(G.johnson())
