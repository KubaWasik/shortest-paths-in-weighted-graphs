import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# funkcja dla gęstości 0.8 - bez sprawdzania
def bellman_ford_08_no_check(x, a, b, c, d):
    return [(0.4 * a) * (pow(v, 3)) - (0.8 * b) * pow(v, 2) + (0.4 * c) * v + d for v in x]


# funkcja dla gęstości 0.8 - ze sprawdzaniem
def bellman_ford_08(x, a, b, c):
    return [(0.4 * a) * (pow(v, 3)) - (0.4 * b) * pow(v, 2) + c for v in x]


# funkcja dla gęstości 0.8
def dijkstra_08(x, a, b, c):
    return [(0.4 * a * np.log10(v)) * (pow(v, 2)) - (0.4 * b * np.log10(v)) * v + c for v in x]


print("Algorytm Bellmana-Forda bez sprawdzania ujemnych cykli")
make_plot("../generated_graphs/density_0.4.graph", "bellman_ford_no_check", 20, "r", bellman_ford_08_no_check)
print("wykres << bellman-ford bez sprawdzania")
make_plot("../generated_graphs/density_0.4.graph", "bellman_ford", 20, "g", bellman_ford_08)
print("wykres << bellman-ford ze sprawdzaniem")
make_plot("../generated_graphs/density_0.4.graph", "dijkstra", 20, "b", dijkstra_08)
print("wykres << dijkstra")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Bellman_Ford_bez_sprawdzania.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Bellman_Ford_bez_sprawdzania.pdf\"")
plt.show()
