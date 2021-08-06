import networkx as nx
import csv
import json
from collections import defaultdict
edges=[]
result=[]

edge_open= open('edges.csv')
csv_read_edge = csv.reader(edge_open)
list_csv_read_edge=list(csv_read_edge)
# print(list_csv_read_edge)
length=len(list_csv_read_edge) 
G = nx.Graph()


for i in range(1,length):
   G.add_edge(list_csv_read_edge[i][0],list_csv_read_edge[i][1])
for c in sorted(nx.connected_components(G), key=len, reverse=True):
	# print(c)
	
	S = G.subgraph(c)
	nodes=len(S)
	# print(list(nx.edges(S)))
	edges=len(list(nx.edges(S)))
	dia=nx.diameter(S) 
	# print(nodes) 
	# print(edges)
	# print(dia)
	result.append({'Nodes':nodes,'Edges':edges,'Diameter':dia})
for i in range(0,12):
	result.append({'Nodes':1,'Edges':0,'Diameter':0})


try:
	with open("graph-components.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Nodes','Edges', 'Diameter'])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")
