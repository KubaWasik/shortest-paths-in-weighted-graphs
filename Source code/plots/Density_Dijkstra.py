import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# funkcja dla gęstości 0.1
def dijkstra_01(x, a, b, c):
    return [(0.1 * a * np.log10(v)) * (pow(v, 2)) - (0.1 * b * np.log10(v)) * v + c for v in x]


# funkcja dla gęstości 0.4
def dijkstra_04(x, a, b, c):
    return [(0.4 * a * np.log10(v)) * (pow(v, 2)) - (0.4 * b * np.log10(v)) * v + c for v in x]


# funkcja dla gęstości 0.8
def dijkstra_08(x, a, b, c):
    return [(0.8 * a * np.log10(v)) * (pow(v, 2)) - (0.8 * b * np.log10(v)) * v + c for v in x]


print("Algorytm Dijkstry, wykres w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "dijkstra", 200, "r", dijkstra_01, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "dijkstra", 200, "g", dijkstra_04, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "dijkstra", 200, "b", dijkstra_08, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Dijkstra_gęstości.pdf", dpi=300, quality=100, format="pdf")
print("wykres zapisany jako \"Wykres_Dijkstra_gęstości.pdf\"")
plt.show()
