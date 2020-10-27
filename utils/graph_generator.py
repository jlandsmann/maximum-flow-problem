import networkx as nx
import random

class GraphGenerator:
    @staticmethod
    def generate():
        graph = nx.DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(15):
            start = random.randint(0, 10)
            end = random.randint(0, 10)
            weight = random.randint(0, 10) / 10
            graph.add_weighted_edges_from([(start, end, weight)])
        return graph
