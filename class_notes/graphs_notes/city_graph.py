# Shortest path from wellsville to smithfield

### Create graph: 
edges = []

for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = int(weight)
    edges.append((node1, node2, weight)) # add edge to a list of tuples
    
print(edges)
g.add_weighted_edges_from(edges) 


### Traverse: 

for n1, n2 in permutations(g.nodes,2): #permutations returns all pairs
    print("all existing paths from", n1, "to", n2, ":")
    
    # all_simple_paths function below returns each path as a list
    # the graph can be accessed with the nodes as keys, like a dictionary
    # g['v0']['v1']['weight'] returns 2, the weight of that edge
    # iterating through the edges in a path, you can calculate the weight of the entire path
    
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path) # print each path
        path_weight = 0
        
        # iterating through each edge in the path and adding edge weight to total path weight
        for i in range(len(path) - 1):
            path_weight += g[path[i]][path[i+1]]['weight']
            current_path_weight
            if path_weight < current_path_weight: 
                current_path_weight = path_weight
        print("path_weight: ", path_weight)

