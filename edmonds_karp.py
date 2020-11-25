import networkx as nx
import numpy as np

from edmonds_karp_path_finder import EdmondsKarpPathFinder


class EdmondsKarp:
    graph_: nx.DiGraph
    source_: int
    sink_: int
    found_sink_ = False

    def __init__(self, graph: nx.DiGraph, source: int, sink: int):
        self.graph_ = graph
        self.source_ = source
        self.sink_ = sink

    def solve(self) -> int:
        path = self.find_augmenting_path()
        total_flow = 0
        while path is not None:
            flow = self.get_capacity_of_path(path)
            self.add_flow_to_path(path, flow)
            total_flow += flow
            path = self.find_augmenting_path()
        return total_flow

    def find_augmenting_path(self) -> list or None:
        path_finder = EdmondsKarpPathFinder(self.graph_, self.source_, self.sink_)
        return path_finder.find_augmenting_path()

    def get_capacity_of_path(self, path: list) -> int:
        path_capacity = np.infty
        for i in range(len(path) - 1):
            edge = self.graph_.edges[path[i], path[i + 1]]
            residual_capacity = edge["capacity"] - edge["flow"]
            path_capacity = min(path_capacity, residual_capacity)
        return path_capacity

    def add_flow_to_path(self, path: list, flow_amount: int) -> None:
        for i in range(len(path) - 1):
            self.add_flow_to_edge(path[i], path[i + 1], flow_amount)

    def add_flow_to_edge(self, u: int, v: int, flow_amount: int) -> None:
        edge = self.graph_.edges[u, v]
        edge["flow"] += flow_amount
        capacity = edge["capacity"]

        if not self.graph_.has_edge(v, u):
            self.graph_.add_edge(v, u, capacity=capacity, flow=capacity)

        reverse_edge = self.graph_.edges[v, u]
        reverse_edge["flow"] -= flow_amount
