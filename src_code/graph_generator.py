"""
Python file with methods for generating a connected graph
"""

# imports
from networkx import Graph
import networkx as nx
import random



######################
# method #
######################



def generate_graph(n, seed=1):

    graph = nx.Graph()
    edge_list = []
    for n_1 in range(n):

        for n_2 in range(n_1+1, n):

            edge_list.append((n_1, n_2))
            
    graph.add_edges_from(edge_list)

    random.seed(seed)
    weights = [random.random() for i in range(len(edge_list))]

    for index, edge in enumerate(graph.edges()):
        graph.get_edge_data(*edge)['weight'] = weights[index]

    return graph, weights