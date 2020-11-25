import networkx as nx
import random
import numpy as np


class GraphGenerator:

    @staticmethod
    def generate(max_nodes=6, max_edges=12, max_weight=5) -> nx.DiGraph:
        graph = nx.DiGraph()
        graph.add_nodes_from(range(1, max_nodes))
        for i in range(1, max_edges):
            start = random.randint(1, max_nodes)
            end = random.randint(1, max_nodes)
            capacity = weight = random.randint(1, max_weight)
            flow = 0
            graph.add_edge(np.minimum(start, end), np.maximum(start, end), weight=weight, capacity=capacity, flow=flow)
        return graph
