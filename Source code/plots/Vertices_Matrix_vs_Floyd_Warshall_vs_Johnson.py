import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# jedna funkcja dla algorytmu opartego o mnożenie macierzy dla wszystkich gęstości - zależność od 1 zmiennej
def matrix(x, a, b):
    return [a * pow(50, 3) * np.log10(50) + b for _ in x]


# jedna funkcja dla algorytmu Floyda-Warshalla dla wszystkich gęstości - zależność od 1 zmiennej
def floyd_warshall(x, a, b):
    return [a * pow(50, 3) + b for _ in x]


# funkcja dla dla algorytmu Johnsona dla stałej ilości wierzchołków
def johnson(x, a, b):
    return [(50 * a) * e + (250 * np.log10(50)) + b for e in x]


print("Porównanie algorytmów z iloczynem odległości, Floyda-Warshalla i Johnsona dla stałej ilości wierzchołków")
make_plot("../generated_graphs/const_50_vertices.graph", "faster_matrix_multiply", 20, "r", count_edges=True, use_polyfit=True)
print("wykres << matrix")
make_plot("../generated_graphs/const_50_vertices.graph", "floyd_warshall", 20, "g", count_edges=True, use_polyfit=True)
print("wykres << Floyd-Warshall")
make_plot("../generated_graphs/const_50_vertices.graph", "johnson", 20, "b", count_edges=True, use_polyfit=True)
print("wykres << Johnson")

plt.xlabel("liczba krawędzi")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_stałe_wierzchołki_Matrix_Floyd_Warshall_Johnson.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_stałe_wierzchołki_Matrix_Floyd_Warshall_Johnson.pdf\"")
plt.show()
