import matplotlib.pyplot as plt
from plots.make_plot import make_plot


# jedna funkcja dla wszystkich gęstości - zależność od 1 zmiennej
def floyd_warshall(x, a, b):
    return [a * pow(v, 3) + b for v in x]


print("Algorytm Floyda-Warshalla, w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "floyd_warshall", 20, "r", floyd_warshall, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "floyd_warshall", 20, "g", floyd_warshall, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "floyd_warshall", 20, "b", floyd_warshall, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Floyd_Warshall_gęstości.pdf", dpi=300, quality=100, format="pdf")
print("Wykres został zapisany do pliku \"Wykres_Floyd_Warshall_gęstości.pdf\"")
plt.show()
