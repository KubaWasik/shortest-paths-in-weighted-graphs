import matplotlib.pyplot as plt
from plots.make_plot import make_plot


print("Algorytm Dijkstry, porównanie implementacji naiwnej oraz z użyciem kolejki priorytetowej")
make_plot("../generated_graphs/const_380_edges.graph", "dijkstra_naive", 100, "r", use_polyfit=True, dim=3)
print("wykres << dijkstra_naive")
make_plot("../generated_graphs/const_380_edges.graph", "dijkstra", 100, "g", use_polyfit=True, dim=3)
print("wykres << dijkstra (kolejka)")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Dijkstra_naiwny_kolejka.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Dijkstra_naiwny_kolejka.pdf\"")
plt.show()
