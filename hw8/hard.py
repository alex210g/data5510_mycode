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



def count_node_degree(g):
    count_nodes = 0
    for node in g:
        #checks if the degree of each node is greater than 5. 
        if g.degree(node) > 5:
            count_nodes = count_nodes + 1
    return count_nodes

print ("Number of nodes in the graph: ", count_node_degree(g))


# AI Prompt USED: How do I access a nodes degree, I had previously included weights in the if statement on line 45 by mistake, it just told me I needed to remove that. That was all. 
