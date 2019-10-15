import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# funkcja dla gęstości 0.8
def dijkstra_all(x, a, b, c):
    return [v * ((0.4 * a * np.log10(v)) * (pow(v, 2)) - (0.4 * b * np.log10(v)) * v + c) for v in x]


# funkcja dla gęstości 0.8
def johnson(x, a, b, c):
    return [(0.4 * a * np.log10(v)) * pow(v, 3) - (0.4 * b * np.log10(v)) * pow(v, 2) + c for v in x]


def floyd_warshall(x, a, b):
    return [a * pow(v, 3) + b for v in x]


print("Algorytm Dijkstry dla wszystkich wierzchołków, porównanie z algorytmami Johnsona i Floyda-Warshalla")
make_plot("../generated_graphs/density_0.4.graph", "dijkstra_all_vertices", 20, "r", dijkstra_all)
print("wykres << dijkstra_all")
make_plot("../generated_graphs/density_0.4.graph", "johnson", 20, "g", johnson)
print("wykres << johnson")
make_plot("../generated_graphs/density_0.4.graph", "floyd_warshall", 20, "b", floyd_warshall)
print("wykres << floyd-warshall")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Dijkstra_all_vs_Johnson.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Dijkstra_all_vs_Johnson.pdf\"")
plt.show()
