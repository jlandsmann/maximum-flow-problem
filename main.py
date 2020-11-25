import time

from utils.edmonds_karp import EdmondsKarp
from utils.graph_generator import GraphGenerator
from utils.max_flow_problem_solver import MaxFlowProblemSolver

max_node_count = 1000
max_edge_count = 6000

print("generation")
start = time.time()
G = GraphGenerator.generate(max_nodes=max_node_count, max_edges=max_edge_count, max_weight=60)
# GraphPrinter.print_graph(G)
end = time.time()
print(end - start)

# print("simple implementation")
# start = time.time()
# solver = MaxFlowProblemSolver(G.copy())
# print(solver.solve(1, max_node_count))
# end = time.time()
# print(end - start)

print("edmonds karp")
start = time.time()
solver = EdmondsKarp(G.copy(), 1, max_node_count)
print(solver.solve())
end = time.time()
print(end - start)
