from utils.graph_generator import GraphGenerator
from utils.graph_printer import GraphPrinter
from utils.max_flow_problem_solver import MaxFlowProblemSolver
from utils.edmonds_karp import EdmondsKarp

G = GraphGenerator.generate(max_nodes=6, max_edges=30, max_weight=20)
GraphPrinter.print_graph(G)
solver = MaxFlowProblemSolver(G.copy())
print(solver.solve(1, 6))

solver = EdmondsKarp(G.copy(), 1, 6)
print(solver.solve())
