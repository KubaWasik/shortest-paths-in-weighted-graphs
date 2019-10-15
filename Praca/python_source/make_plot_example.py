import matplotlib.pyplot as plt
from described.graph import Graph, Edge, Vertex
from plots.make_plot import make_plot

make_plot("const_380_edges.graph", 
          "dijkstra_naive", 100, "r", 
          use_polyfit=True, dim=3)
make_plot("const_380_edges.graph", 
          "dijkstra", 100, "g", 
          use_polyfit=True, dim=3)

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.legend()
plt.grid()
plt.savefig(fname="Wykres_Dijkstra_naiwny_kolejka.pdf", 
            dpi=300, quality=100, format="pdf")
plt.show()