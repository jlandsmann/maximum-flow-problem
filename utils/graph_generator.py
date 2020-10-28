import networkx as nx
import random
import numpy as np


class GraphGenerator:

    @staticmethod
    def generate(max_nodes=6, max_edges=12, max_weight=5) -> nx.DiGraph:
        graph = nx.DiGraph()
        for i in range(1, max_nodes):
            graph.add_node(i)
        for i in range(1, max_edges):
            start = random.randint(1, max_nodes)
            end = random.randint(1, max_nodes)
            weight = random.randint(1, max_weight)
            graph.add_weighted_edges_from([(np.minimum(start, end), np.maximum(start, end), weight)])
        return graph
