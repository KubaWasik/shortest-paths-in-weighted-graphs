import matplotlib.pyplot as plt
import numpy as np
from plots.make_plot import make_plot


# funkcja dla gęstości 0.1
def johnson_01(x, a, b, c):
    return [(0.1 * a * np.log10(v)) * pow(v, 3) - (0.1 * b * np.log10(v)) * pow(v, 2) + c for v in x]


# funkcja dla gęstości 0.4
def johnson_04(x, a, b, c):
    return [(0.4 * a * np.log10(v)) * pow(v, 3) - (0.4 * b * np.log10(v)) * pow(v, 2) + c for v in x]


# funkcja dla gęstości 0.8
def johnson_08(x, a, b, c):
    return [(0.8 * a * np.log10(v)) * pow(v, 3) - (0.8 * b * np.log10(v)) * pow(v, 2) + c for v in x]


print("Algorytm Johnsona, w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "johnson", 20, "r", johnson_01, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "johnson", 20, "g", johnson_04, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "johnson", 20, "b", johnson_08, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Johnson_gęstości.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Johnson_gęstości.pdf\"")
plt.show()
