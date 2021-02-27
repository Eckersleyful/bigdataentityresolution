import itertools

def create_blocking_graph(blocks):
    #first we create the nodes
    graph_nodes = []
    edges = []
    for block in blocks:
        for some_entity in block:
            if some_entity not in graph_nodes:
                graph_nodes.append(some_entity)
    
        #Then we create all possible pairs of entities from one block and make them into edges
        #we use itertools permutation for easy way of generating all pairs
        #blocks[block] here is a list of all the token-blocked entities 
        possible_permutations = itertools.permutations(blocks[block], 2)
        for permutation in possible_permutations:
            
            #create a new edge and force it into a set because itertools creates pairs
            #like "dog, cat" "cat, dog" which we dont want, set makes lists have only unique values
            new_edge = set((permutation[0], permutation[1]))
            
            #make sure that the edge is a pair and that its not found before
            if new_edge not in edges and len(new_edge) == 2:
                edges.append(new_edge)
    return (graph_nodes, edges)