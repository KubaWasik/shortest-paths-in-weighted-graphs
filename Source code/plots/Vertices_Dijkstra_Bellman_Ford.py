import matplotlib.pyplot as plt
from plots.make_plot import make_plot


print("Porównanie algorytmów Dijkstry i Bellmana-Forda dla stałej ilości wierzchołków")
make_plot("../generated_graphs/const_50_vertices.graph", "dijkstra", 100, "g", count_edges=True, use_polyfit=True)
print("wykres << Dijkstra")
make_plot("../generated_graphs/const_50_vertices.graph", "bellman_ford", 100, "b", count_edges=True, use_polyfit=True)
print("wykres << Bellman-Ford")

plt.xlabel("liczba krawędzi")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_stałe_wierzchołki_Dijkstra_Bellman_Ford.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_stałe_wierzchołki_Dijkstra_Bellman_Ford.pdf\"")
plt.show()
