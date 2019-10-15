import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# jedna funkcja dla algorytmu Floyda-Warshalla dla wszystkich gęstości - zależność od 1 zmiennej
def floyd_warshall(x, a, b):
    return [a * pow(v, 3) + b for v in x]


# funkcja dla dla algorytmu Johnsona dla stałej ilości wierzchołków
def johnson(x, a, b, c):
    return [(a * pow(v, 2)) * np.log10(v) + (380 * b * v) + c for v in x]


print("Porównanie algorytmów Floyda-Warshalla i Johnsona dla stałej ilości krawędzi")
make_plot("../generated_graphs/const_380_edges.graph", "floyd_warshall", 20, "g", floyd_warshall)
print("wykres << Floyd-Warshall")
make_plot("../generated_graphs/const_380_edges.graph", "johnson", 20, "b", johnson)
print("wykres << Johnson")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_stałe_krawędzie_Floyd_Warshall_Johnson.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_stałe_krawędzie_Floyd_Warshall_Johnson.pdf\"")
plt.show()
