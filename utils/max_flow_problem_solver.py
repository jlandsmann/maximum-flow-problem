import math
import numpy as np
import networkx as nx


class MaxFlowProblemSolver:
    graph_: nx.DiGraph

    def __init__(self, graph: nx.DiGraph):
        self.graph_ = graph


    def solve(self, source, sink) -> int:
        flow = 0
        ran_paths = []
        path = self.find_path(source, sink)
        while path is not None:
            flow += self.generate_residual_graph(path)
            ran_paths.append(path)
            path = self.find_path(source, sink, [], ran_paths)
        return flow

    def find_path(self, source, sink, path: list = None, paths_to_ignore: list = None):
        if path is None:
            path = []
        path.append(source)

        if paths_to_ignore is None:
            paths_to_ignore = []

        if path in paths_to_ignore:
            return None

        if source == sink:
            return path
        successors = self.graph_.successors(source)
        for successor in successors:
            if successor in path:
                continue
            possible_path = self.find_path(successor, sink, path.copy(), paths_to_ignore)
            if possible_path is not None:
                return possible_path
        return None

    def get_max_flow(self, path: list) -> int:
        path_length = len(path)
        max_flow = math.inf
        for i in range(path_length - 1):
            u = path[i]
            v = path[i + 1]
            if not self.graph_.has_edge(u, v):
                return 0
            data = self.graph_.get_edge_data(u, v)
            weight = data["weight"]
            max_flow = np.minimum(weight, max_flow)
        return max_flow

    def generate_residual_graph(self, path) -> int:
        flow = self.get_max_flow(path)
        if flow <= 0:
            return 0
        path_length = len(path)
        for i in range(path_length - 1):
            u = path[i]
            v = path[i + 1]
            if not self.graph_.has_edge(u, v):
                return 0
            if not self.graph_.has_edge(v, u):
                self.graph_.add_edge(v, u, weight=0)
            self.graph_[u][v]["weight"] -= flow
            self.graph_[v][u]["weight"] += flow
        return flow
