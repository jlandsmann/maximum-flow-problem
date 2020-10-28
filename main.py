from utils.graph_generator import GraphGenerator
from utils.graph_printer import GraphPrinter
from utils.max_flow_problem_solver import MaxFlowProblemSolver

G = GraphGenerator.generate(max_nodes=6, max_edges=30, max_weight=20)
GraphPrinter.print_graph(G)
# GraphPrinter.print_edges(G)
solver = MaxFlowProblemSolver(G)
print(solver.solve(1, 6))
