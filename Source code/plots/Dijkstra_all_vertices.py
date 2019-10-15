import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# funkcja dla gęstości 0.1
def dijkstra_all_01(x, a, b, c):
    return [v * ((0.1 * a * np.log10(v)) * (pow(v, 2)) - (0.1 * b * np.log10(v)) * v + c) for v in x]


# funkcja dla gęstości 0.4
def dijkstra_all_04(x, a, b, c):
    return [v * ((0.4 * a * np.log10(v)) * (pow(v, 2)) - (0.4 * b * np.log10(v)) * v + c) for v in x]


# funkcja dla gęstości 0.8
def dijkstra_all_08(x, a, b, c):
    return [v * ((0.8 * a * np.log10(v)) * (pow(v, 2)) - (0.8 * b * np.log10(v)) * v + c) for v in x]


print("Algorytm Dijkstry dla wszystkich wierzchołków, wykres w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "dijkstra_all_vertices", 10, "r", dijkstra_all_01, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "dijkstra_all_vertices", 10, "g", dijkstra_all_04, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "dijkstra_all_vertices", 10, "b", dijkstra_all_08, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Dijkstra_wszystkie_wierzchołki.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Dijkstra_wszystkie_wierzchołki.pdf\"")
plt.show()
