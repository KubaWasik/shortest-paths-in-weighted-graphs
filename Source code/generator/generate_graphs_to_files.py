import pickle

from described.graph import Graph
from generator.graph_generator import generate

print("\nGenerator grafów\n")
print("1. stała liczba krawędzi rośnie liczba wierzchołków (start: 20 wierzchołków i maksymalna liczby krawędzi)\n")
with open("../generated_graphs/const_380_edges.graph", "wb") as graph_file:
    graphs_list = []
    edges_number = 380
    for i in range(20, 70):
        g: Graph = generate(i, edges_number)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("2.stała liczba wierzchołków (np. 50) i rośnie liczba krawędzi (zagęszczanie grafu)\n")
with open("../generated_graphs/const_50_vertices.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(0, 2450, 50):
        g: Graph = generate(50, i)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("3.rośnie jedno i drugie (np. może być zachowana stała gęstość)\n" +
      "----------------------------------------------------------------\n" +
      "- zbiór grafów o gęstości 0.1\n")
with open("../generated_graphs/density_0.1.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(5, 55):
        g: Graph = generate(i, int((i * (i - 1)) / 10))
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("- zbiór grafów o gęstości 0.4\n")
with open("../generated_graphs/density_0.4.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(5, 55):
        g: Graph = generate(i, 4 * int((i * (i - 1)) / 10))
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("- zbiór grafów o gęstości 0.8\n")
with open("../generated_graphs/density_0.8.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(5, 55):
        g: Graph = generate(i, 8 * int((i * (i - 1)) / 10))
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("------------------------------------------------------------\n" +
      "znalezienie \"granicy\" rzadkiego grafu:\n" +
      "0. stała liczba wierzchołków: 10 i rośnie liczba krawędzi (zagęszczanie grafu) z przedziału <0;20>\n")
with open("../generated_graphs/const_10_vertices_edges_0_20.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(0, 20):
        g: Graph = generate(10, i)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("1. stała liczba wierzchołków: 50 i rośnie liczba krawędzi (zagęszczanie grafu) z przedziału <0;300>\n")
with open("../generated_graphs/const_50_vertices_edges_0_250.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(0, 250, 5):
        g: Graph = generate(50, i)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("2. stała liczba wierzchołków: 100 i rośnie liczba krawędzi (zagęszczanie grafu) z przedziału <0;1000>\n")
with open("../generated_graphs/const_100_vertices_edges_0_1000.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(0, 1000, 20):
        g: Graph = generate(100, i)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("3. stała liczba wierzchołków: 150 i rośnie liczba krawędzi (zagęszczanie grafu) z przedziału <0;2250>\n")
with open("../generated_graphs/const_150_vertices_edges_0_2250.graph", "wb") as graph_file:
    graphs_list = []
    for i in range(0, 2250, 45):
        g: Graph = generate(150, i)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)

print("Wygenerowano wszystkie grafy i zapisano pliki w folderze \"generated_graphs\"")
