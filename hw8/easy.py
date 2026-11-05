import os
import matplotlib

matplotlib.use('Agg') # putting matplolib into server-only mode, no GUI


import networkx as nx



############################################################
# Loading edges of the Graph from a file: example_graph.png
curr_dir = os.path.dirname(__file__) # get the current directory of this file

edges_fil = curr_dir + "/" + "edges.txt" # dirname and __file__ (this file) returns the current folder
# graph_visual_fil = curr_dir + "/" + "graph_visual.png"

file = open(edges_fil) 

g = nx.DiGraph() # created directed graph



############################################################
# STEP 1 - Create Graph
# get all edges from the txt file
edges = []

for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = int(weight)
    edges.append((node1, node2, weight)) # add edge to a list of tuples
    
print(edges)
g.add_weighted_edges_from(edges) 

# print all nodes
print(g.nodes)

######################################
# Count the number of nodes in the graph 

def count_nodes_in_graph(g):
    count_nodes = 0
    #iterate through the graph
    for node in g:
        #if there is a node, count it. 
        count_nodes = count_nodes + 1
    return count_nodes

print ("Number of nodes in the graph: ", count_nodes_in_graph(g))



############################################################
# AI PROMPTS USED
#
# Prompt 1: "I have setup a for loop to iterate through the g.node, but my count is not working. What is the item that I want to count? Is it not g.node?"
# Prompt 2: "Create a txt file of nodes and can you make it comma separated and have no spaces?" This was done for creating data for edges.txt.
# Prompt 3: "How many nodes should be in that?" Asked to verify my output was correct. 
# Prompt 4: "So why can I not put g.nodes into the argument position? That is what actually contains the graph no?"
