import networkx as nx
import matplotlib.pyplot as plt

from utils.graph_generator import GraphGenerator

G = GraphGenerator.generate()
plt.subplot()
layout = nx.shell_layout(G, scale=5)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos=layout, with_labels=True, font_color='w', font_size=9)
nx.draw_networkx_edge_labels(G, pos=layout, font_size=8, edge_labels=edge_labels)
plt.show()