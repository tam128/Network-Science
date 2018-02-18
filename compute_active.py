import argparse
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

node_list=[]
active_list=[]

#Get input .csv file, px, and results filename
parser = argparse.ArgumentParser()
parser.add_argument("input_graph", help="input .csv file for directed graph")
parser.add_argument("px", type=int, help="activation probability")
parser.add_argument("results_file", help="output file for results")
args = parser.parse_args()

df = pd.read_csv(args.input_graph, sep=',', engine='python')
g = nx.DiGraph()

#Create graph with list of nodes and edges
for index, row in df.iterrows():
	n1 = df.iloc[index, 0]
	n2 = df.iloc[index, 1]
	if n1 not in node_list:
		node_list.append(n1)
		g.add_node(n1)
	if n2 not in node_list:
		node_list.append(n2)
		g.add_node(n1)
	g.add_edge(n1, n2)

#Output list of activated nodes
with open(args.results_file, 'w') as outfile:
	writer = csv.writer(outfile, lineterminator = '\n')	
	#Breadth first search
	for target_node in list(g.nodes()):
		visited, queue = set(), [target_node]
		num_active = 0
		while queue:
			vertex = queue.pop(0)
			next_node = g[vertex]
			if vertex not in visited and vertex % args.px == 0 or vertex==target_node:
				visited.add(vertex)
				queue.extend(list(g.neighbors(vertex)))
				num_active+=1
		active_list.append([target_node, num_active])
	#If there is a tie in number of activated nodes, sort by nodeID
	active_list = sorted(active_list, key=lambda tup: tup[0])
	#Sort in descending order by number of activated nodes
	active_list = sorted(active_list, key=lambda tup: tup[1], reverse=True)
	
	for x in active_list:
		writer.writerow([x[0], x[1]])	

