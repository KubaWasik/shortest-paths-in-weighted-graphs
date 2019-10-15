import matplotlib.pyplot as plt
from plots.make_plot import make_plot


# funkcja dla gęstości 0.1
def bellman_ford_01(x, a, b, c):
    return [(0.1 * a) * (pow(v, 3)) - (0.1 * b) * pow(v, 2) + c for v in x]


# funkcja dla gęstości 0.4
def bellman_ford_04(x, a, b, c):
    return [(0.4 * a) * (pow(v, 3)) - (0.4 * b) * pow(v, 2) + c for v in x]


# funkcja dla gęstości 0.8
def bellman_ford_08(x, a, b, c):
    return [(0.8 * a) * (pow(v, 3)) - (0.8 * b) * pow(v, 2) + c for v in x]


print("Algorytm Bellmana-Forda, wykres w zależności od gęstości grafu")
make_plot("../generated_graphs/density_0.1.graph", "bellman_ford", 20, "r", bellman_ford_01, density=0.1)
print("wykres << gęstość 0.1")
make_plot("../generated_graphs/density_0.4.graph", "bellman_ford", 20, "g", bellman_ford_04, density=0.4)
print("wykres << gęstość 0.4")
make_plot("../generated_graphs/density_0.8.graph", "bellman_ford", 20, "b", bellman_ford_08, density=0.8)
print("wykres << gęstość 0.8")

plt.xlabel("liczba wierzchołków")
plt.ylabel("czas (s)")
plt.grid()
plt.savefig(fname="pdf_files/Wykres_Bellman_Ford_gęstości.pdf", dpi=300, quality=100, format="pdf")
print("wykres zapisany jako \"Wykres_Bellman_Ford_gęstości.pdf\"")
plt.show()
