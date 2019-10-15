import pickle
from timeit import Timer

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def make_plot(file_name: str, function_name: str,
              repeat_number: int, color: str,
              approximation_function=None,
              count_edges: bool = False,
              count_vertices: bool = False,
              density: float = None, 
              use_polyfit: bool = False,
              dim: int = 1):
    with open(file_name, "rb") as graph_file:
        graphs_list = pickle.load(graph_file)

    data = {}
    for graph in graphs_list:
        function = getattr(graph, function_name)
        t = Timer(lambda: function())
        function_time = t.repeat(repeat_number, 1)
        function_time = min(function_time)

        if count_edges is False and count_vertices \
                is False:
            count_vertices = True
        if count_edges is True and count_vertices \
                is True:
            print("Błąd, nie można liczyć krawędzi \
            i wierzchołków jednocześnie")
            return

        if count_vertices:
            data[len(graph.vertices)] = function_time
        elif count_edges:
            data[len(graph.edges)] = function_time

    x_array = [x for x in data]
    y_array = []
    for x in x_array:
        y_array.append(data[x])

    plt.plot(x_array, y_array, '.')

    if use_polyfit:
        z = np.polyfit(x_array, y_array, dim)
        p = np.poly1d(z)
        plt.plot(x_array, p(x_array), color, label="{}"
                 .format(str(function_name)))
    else:
        popt, pcov = curve_fit(approximation_function,
                               x_array, y_array)
        if density is None:
            plt.plot(x_array, approximation_function(
                x_array, *popt), color, label="{}"
                     .format(str(function_name)))
        else:
            plt.plot(x_array, approximation_function(
               x_array, *popt), color,
               label="gęstość {}".format(str(density)))
