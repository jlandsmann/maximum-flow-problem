from queue import SimpleQueue
import networkx as nx


class EdmondsKarpPathFinder:
    graph_: nx.DiGraph
    source_: int
    sink_: int

    found_sink_ = False
    predecessors = {}
    nodes_to_scan = SimpleQueue()
    nodes_to_ignore = []

    def __init__(self, graph: nx.DiGraph, source: int, sink: int):
        self.graph_ = graph
        self.source_ = source
        self.sink_ = sink
        self.nodes_to_scan.put(self.source_)
        self.found_sink_ = False

    def find_augmenting_path(self) -> list or None:
        while not self.nodes_to_scan.empty() and not self.found_sink_:
            node_to_scan = self.nodes_to_scan.get()
            self.scan_node(node_to_scan)

        if not self.found_sink_:
            return None
        return self.get_path_from_predecessors(self.source_, self.sink_, self.predecessors)

    def is_node_already_labeled(self, node_to_label: int) -> bool:
        return self.predecessors.get(node_to_label) is not None \
               or self.nodes_to_ignore.__contains__(node_to_label)

    def label_node(self, current_node: int, node_to_label: int):
        edge: dict = self.graph_.edges[current_node, node_to_label]
        residual_capacity = edge["capacity"] - edge["flow"]
        if not self.is_node_already_labeled(node_to_label) and residual_capacity > 0:
            self.predecessors[node_to_label] = current_node
            if node_to_label == self.sink_:
                self.found_sink_ = True
            self.nodes_to_ignore.append(node_to_label)
            self.nodes_to_scan.put(node_to_label)

    def scan_node(self, node_to_scan: int):
        for successor in self.graph_.successors(node_to_scan):
            if self.found_sink_:
                break
            if successor == node_to_scan:
                continue
            self.label_node(node_to_scan, successor)

    @staticmethod
    def get_path_from_predecessors(first_node: int, last_node: int, predecessors: dict) -> list:
        path = []
        node = last_node
        while node != first_node:
            path.append(node)
            node = predecessors[node]
        path.append(node)
        path.reverse()
        return path
