import matplotlib.pyplot as plt
import numpy as np
from all import Graph, Edge, Vertex
from wykresy.make_plot import make_plot


# jedna funkcja dla algorytmu opartego o mnożenie macierzy dla wszystkich gęstości - zależność od 1 zmiennej
def matrix(x, a, b, c):
    return [(a * pow(v, 3)) * (b * np.log10(v)) + c for v in x]


# jedna funkcja dla algorytmu Floyda-Warshalla dla wszystkich gęstości - zależność od 1 zmiennej
def floyd_warshall(x, a, b):
    return [a * pow(v, 3) + b for v in x]


# funkcja dla dla algorytmu Johnsona dla stałej ilości wierzchołków
def johnson(x, a, b, c):
    return [(380 * a * v) * (b * np.log10(v)) + c for v in x]


print("Porównanie algorytmów z iloczynem odległości, Floyda-Warshalla i Johnsona dla stałej ilości krawędzi")
make_plot("graphs/const_380_edges.graph", "faster_matrix_multiply", 15, "r", matrix)
print("wykres << matrix")
make_plot("graphs/const_380_edges.graph", "floyd_warshall", 20, "g", floyd_warshall)
print("wykres << Floyd-Warshall")
make_plot("graphs/const_380_edges.graph", "johnson", 20, "b", johnson)
print("wykres << Johnson")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
# plt.legend()
plt.grid()
plt.savefig(fname="plots/Wykres_stałe_krawędzie_Matrix_Floyd_Warshall_Johnson.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_stałe_krawędzie_Matrix_Floyd_Warshall_Johnson.pdf\"")
plt.show()
