import pandas as pd
import json
from collections import defaultdict
import csv
with open('neighbor-district-modified.json') as json_file:
    data = json.load(json_file)
graph = defaultdict(list)
def add_edge_in_graph(graph,u,v):
    graph[u].append(v)
 
# definition of function
def edges_create(graph):
    edges = []
 
    # for each node in graph
    for node in graph:
            # for each neighbour node 
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
 
# declaration of graph as dictionary
for dis,neigh_dist_list in data.items():
    for neigh_dis in neigh_dist_list:
        add_edge_in_graph(graph,dis,neigh_dis)

que3 = pd.DataFrame(edges_create(graph), columns=['district', 'neighbor'])
que3.to_csv('edge-graph.csv')
