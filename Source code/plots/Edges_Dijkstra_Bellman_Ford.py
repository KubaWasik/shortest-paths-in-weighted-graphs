import matplotlib.pyplot as plt
from plots.make_plot import make_plot


print("Porównanie algorytmów Dijkstry i Bellmana-Forda dla stałej ilości krawędzi")
make_plot("../generated_graphs/const_380_edges.graph", "dijkstra", 100, "g", use_polyfit=True)
print("wykres << Dijkstra")
make_plot("../generated_graphs/const_380_edges.graph", "bellman_ford", 100, "b", use_polyfit=True)
print("wykres << Bellman-Ford")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_stałe_krawędzie_Dijkstra_Bellman_Ford.pdf", dpi=300, quality=100, format="pdf")
plt.show()
print("Wykres został zapisany do pliku \"Wykres_stałe_krawędzie_Dijkstra_Bellman_Ford.pdf\"")
