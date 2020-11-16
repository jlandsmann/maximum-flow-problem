import numpy as np
from queue import SimpleQueue
import networkx as nx

class EdmondsKarp:
    graph_: nx.DiGraph
    source_: str
    sink_: str

    def __init__(self, graph: nx.DiGraph, source: str, sink: str):
        self.graph_ = graph
        self.source_ = source
        self.sink_ = sink

    def find_augmenting_path(self):
        # if a node is contained, the node is labeled
        # if an other node links to a node, the node is scanned
        predecessors = []
        labeled_nodes = SimpleQueue()
        labeled_nodes.put(self.source_)
        found_sink = False

        while not labeled_nodes.empty() and not found_sink:
            current_node = labeled_nodes.get()
            for successor in self.graph_.successors(current_node):
                edge = self.graph_.edges[current_node, successor]
                if predecessors[successor] is None and successor != self.source_ and edge["capacity"] > edge["flow"]:
                    predecessors[successor] = current_node
                    if successor == self.sink_:
                        found_sink = True
                        break
                    labeled_nodes.put(successor)

        path = []
        node = self.sink_
        while node != self.source_:
            path.append(node)
            node = predecessors[node]
        return path.reverse()
