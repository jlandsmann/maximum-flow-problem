from queue import SimpleQueue

import networkx as nx
import numpy as np


class EdmondsKarp:
    graph_: nx.DiGraph
    source_: int
    sink_: int

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
        # breadth-first search for sink, returning shortest path from source to sink
        predecessors = {}
        labeled_nodes = SimpleQueue()
        labeled_nodes.put(self.source_)
        nodes_to_ignore = []
        found_sink = False

        while not labeled_nodes.empty() and not found_sink:
            current_node = labeled_nodes.get()
            for successor in self.graph_.successors(current_node):
                if found_sink:
                    break
                if successor == current_node:
                    continue
                edge: dict = self.graph_.edges[current_node, successor]
                if predecessors.get(successor) is None and successor != self.source_ and edge["capacity"] > edge["flow"] and not nodes_to_ignore.__contains__(successor):
                    predecessors[successor] = current_node
                    if successor == self.sink_:
                        found_sink = True
                    nodes_to_ignore.append(successor)
                    labeled_nodes.put(successor)

        if not found_sink:
            return None
        path = []
        node = self.sink_
        while node != self.source_:
            path.append(node)
            node = predecessors[node]
        path.append(node)
        path.reverse()
        return path

    def get_capacity_of_path(self, path: list) -> int:
        capacity = np.infty
        for i in range(len(path) - 1):
            edge = self.graph_.edges[path[i], path[i + 1]]
            capacity = min(capacity, edge["capacity"] - edge["flow"])
        return capacity

    def add_flow_to_path(self, path: list, flow_amount: int) -> None:
        for i in range(len(path) - 1):
            edge = self.graph_.edges[path[i], path[i + 1]]
            edge["flow"] += flow_amount

            if not self.graph_.has_edge(path[i+1], path[i]):
                self.graph_.add_edge(path[i+1], path[i], capacity=edge["capacity"], flow=edge["capacity"])
            reverse_edge = self.graph_.edges[path[i+1], path[i]]
            reverse_edge["flow"] -= flow_amount

