import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# jedna funkcja dla wszystkich gęstości - zależność od 1 zmiennej
def matrix(x, a, b):
    return [a * pow(v, 3) * np.log10(v) + b for v in x]


print("Algorytm z iloczynem odległości, w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "faster_matrix_multiply", 20, "r", matrix, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "faster_matrix_multiply", 20, "g", matrix, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "faster_matrix_multiply", 20, "b", matrix, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Macierze_gęstości.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Macierze_gęstości.pdf\"")
plt.show()
