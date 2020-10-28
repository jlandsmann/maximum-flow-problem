import networkx as nx
import numpy as np
import math as math
import matplotlib.pyplot as plt


class GraphPrinter:

    @staticmethod
    def print_edges(g: nx.DiGraph):
        print('#####')
        edges = g.edges
        for edge in edges:
            print(edge)
        print('#####')


    @staticmethod
    def print_graph(g: nx.DiGraph):
        plt.subplot()
        layout = GraphPrinter.get_layout_(g)
        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw(g, pos=layout, with_labels=True, font_color='w', font_size=9)
        nx.draw_networkx_edge_labels(g, pos=layout, font_size=8, edge_labels=edge_labels, label_pos=0.75)
        plt.show()

    @staticmethod
    def get_layout_(g: nx.DiGraph) -> dict:
        # return nx.circular_layout(g)
        node_count = g.number_of_nodes()
        nodeIdx = 1
        max_x = 5
        max_y = math.ceil(node_count / max_x)
        positions = {}
        for x in range(max_x):
            for y in range(max_y):
                if nodeIdx > node_count:
                    break
                positions[nodeIdx] = (x, y)
                nodeIdx += 1

        return positions
