import pickle
from described.graph import Graph
from generator.graph_generator import generate


with open("const_380_edges.graph", "wb") as graph_file:
    graphs_list = []
    edges_number = 380
    for i in range(20, 70):
        g: Graph = generate(i, edges_number)
        graphs_list.append(g)
    pickle.dump(graphs_list, graph_file)
