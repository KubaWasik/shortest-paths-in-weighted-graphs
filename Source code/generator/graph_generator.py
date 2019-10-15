import operator
import random

from described.all_in_one_class_for_generator import Edge, Graph, Vertex


def generate(vertices_number, edges_number):
    print("Generowany graf:")
    print("Liczba wierzchołków: ", vertices_number)
    print("Liczba krawędzi: ", edges_number)
    print("Gęstość grafu: ", edges_number / (vertices_number * (vertices_number - 1)), end="\n\n")
    vertices = []
    for i in range(vertices_number):
        name = ""
        first_letter = int(i / 26)
        second_letter = i % 26
        if first_letter != 0:
            first_letter = chr(97 + first_letter - 1)
            name += first_letter
        second_letter = chr(97 + second_letter)
        name += second_letter
        vertices.append(Vertex(name))
    edges = []
    graph_edges = []
    available_edges = []
    for v_start in vertices:
        for v_end in vertices:
            if v_start == v_end:
                continue
            available_edges.append((v_start, v_end))
    for i in range(edges_number):
        random_edge = random.choice(available_edges)
        edges.append(random_edge)
        available_edges.remove(random_edge)

    for edge in edges:
        start_vertex, end_vertex = edge
        weight = random.randint(0, 10)
        graph_edges.append(Edge(start_vertex.name, end_vertex.name, weight))

    graph_edges.sort(key=operator.attrgetter('start', 'end'))
    graph = Graph(vertices={vertex.name: vertex for vertex in vertices}, edges=graph_edges)
    return graph


if __name__ == "__main__":
    print("Plik zawierający funkcję generatora grafów")
