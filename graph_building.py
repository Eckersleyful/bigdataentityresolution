import itertools
import time 
import math

def create_blocking_graph(blocks):
    #first we create the nodes
    graph_nodes = []
    edges = []
    for block in blocks:
        for some_entity in blocks[block]:

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
    return graph_nodes, edges


def weigh_common_blocks(edge, blocks):
    common_counter = 0
    first_entity = list(edge)[0]
    second_entity = list(edge)[1]
    for block in blocks:
        entities_in_block = blocks[block]
        if first_entity in entities_in_block and second_entity in entities_in_block:
            common_counter += 1
    return common_counter
def calculate_common_blocks_scheme(edges, blocks):
    common_weighted_edges = {}
    current_edge_index = 0
    for edge in edges:
        common_counter = weigh_common_blocks(edge, blocks)
        common_weighted_edges[current_edge_index] = common_counter
        current_edge_index += 1
    return common_weighted_edges    
def get_entity_block_amount(entity, blocks):
    block_amount = 0
    for block in blocks:
        if entity in blocks[block]:
            block_amount += 1
    return block_amount
def calculate_jaccard_blocks_scheme(edges, blocks):
    jaccard_edges = {}
    current_edge_index = 0
    for edge in edges:
        common_blocks = weigh_common_blocks(edge, blocks)
        jaccard_value = common_blocks / ( (get_entity_block_amount(list(edge)[0], blocks) + get_entity_block_amount(list(edge)[1], blocks)) -  common_blocks) 
        jaccard_edges[current_edge_index] = jaccard_value
        current_edge_index += 1
    return jaccard_edges


def weight_edge_pruning(edges, weighted_edges):
    average_weight = get_average_weight_of_edges(edges, weighted_edges)
    temp_edges = edges
    removable_keys = []
    current_edge_index = 0
    for edge in temp_edges:
        if weighted_edges[current_edge_index] < average_weight:
            removable_keys.append(current_edge_index)
        current_edge_index += 1
    for key in removable_keys:
        temp_edges[key] = None
    return temp_edges
def get_average_weight_of_edges(edges, weighted_edges):
    edge_weight_sum = 0
    current_edge_index = 0
    for edge in weighted_edges:
        edge_weight_sum += weighted_edges[current_edge_index]
        current_edge_index += 1
    return edge_weight_sum / len(weighted_edges.keys())

def calculate_neighbor_k(node_neighbors):
    return int(math.ceil(0.1*len(node_neighbors)))

def remove_bad_edges(edges):
    good_edges = []
    for edge in edges:
        if edge is not None:
            good_edges.append(edge)
    return good_edges
def get_node_neighbors(node, edges, weighted_edges):
    #list of tuples where 0 is 
    list_of_neighbor_edges = []
    current_edge_index = 0
    for edge in edges:
        if node == list(edge)[0] or node == list(edge)[1]:
  
           list_of_neighbor_edges.append((current_edge_index, weighted_edges[current_edge_index]))
        current_edge_index += 1    
    return list_of_neighbor_edges

def get_directed_graph_blocks(directed_edge_graph):

    directed_blocks = {}
    for edge in directed_edge_graph:

        #check if the edge root already exists in the dict
        if edge[0] in directed_blocks:
            directed_blocks[edge[0]].append(edge[1])

        else:
            directed_blocks[edge[0]]=  [edge[1]]

    return(directed_blocks)


def calculate_cardinality_node_pruning(nodes, edges, weighted_edges):
    new_directed_edges = []

    for node in nodes:
        #get all neighbouring edges for a node and their weights as a list of tuples
        node_neighbors = get_node_neighbors(node, edges, weighted_edges)
        #sort the neighboring edges of the node by their weight
        sorted_neighbor_weights = sorted(node_neighbors, key = lambda weigh: weigh[1], reverse = True)

        #calculate k-value
        k_value = calculate_neighbor_k(node_neighbors)
        #select k elements from the sorted edges
        k_ranked_node_neighbors = sorted_neighbor_weights[:k_value]
        
        #create directed edges from the k-top edges
        for edge_tuple in k_ranked_node_neighbors:
            #here edge_tuple[0] is the corresponding index found in neighbor creation function
            old_edge = list(edges[edge_tuple[0]])

            #check if the current node is the root of the edge

            if old_edge[0] == node:
                new_directed_edges.append(old_edge)
            else:
                old_edge.reverse()
                new_directed_edges.append(old_edge)

    return new_directed_edges
