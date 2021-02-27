from csv_functions import open_csv
from dict_functions import *
from similarity_functions import jaccard
from graph_building import create_blocking_graph
import time
import itertools

def find_similar_attribute(structure_att_dict, structure_att_dict_2):

    #Find most similar attributes for the structures in the second dataset
    
    #Key in this dict is the attribute and value is the other attribute and currently highest Jaccard similarity index
    #Example: location = ("located at", 0.55)
    similarity_dict = {}
    jaccard_into_dict(similarity_dict, structure_att_dict, structure_att_dict_2)
    jaccard_into_dict(similarity_dict, structure_att_dict_2, structure_att_dict)

    return similarity_dict

def jaccard_into_dict(similarity_dict, dataset, dataset_2):

    for attribute in dataset:
        #place the found values in temp list for jaccard similarity
        attribute_values = get_values_of_attribute(dataset, attribute)
        #print(attribute_values)
        for other_attribute in dataset_2:
            other_attribute_values = get_values_of_attribute(dataset_2, other_attribute)
            
            current_jaccardian_similarity = jaccard(attribute_values, other_attribute_values)
            if attribute in similarity_dict: 
                if current_jaccardian_similarity > similarity_dict[attribute][1]:
                    similarity_dict[attribute] = (other_attribute, current_jaccardian_similarity)
            elif current_jaccardian_similarity > 0:
                similarity_dict[attribute] = (other_attribute, current_jaccardian_similarity)


def transitional_closure_clustering(similarity_dict):
    #The aim here is to find all transitive closure clusters of the attribute pairs in the similarity_dict
    #Because we can think of the similarity dictionary as a directed graph of pairs, where each value
    #is pointing into another one, we can find the transitive closure pairs of the pairs and generate clusters
    #based on them. For example, if A points to B and B points to C, C has also point to A to satisfy reachability.
    #This rule works in the other direction as well
    #Clusters are tuples of attribute names in this implementation
    current_cluster_index = 0
    clusters = {}
    found_pointers = []
    for pair_key in similarity_dict:
        

        current_pair = (pair_key, similarity_dict[pair_key])
        
        if current_cluster_index not in clusters:
            clusters[current_cluster_index] = []
        if not is_in_cluster(current_pair, clusters):
                
                found_pointers.append(current_pair)
                find_pointer_pairs(found_pointers, similarity_dict, current_pair)
         
                clusters[current_cluster_index] = found_pointers
                current_cluster_index += 1
                found_pointers = []
             
    
    return clusters
def is_in_cluster(current_pair, clusters):
    for key in clusters:
        #print(clusters[key], current_pair)
        if current_pair in clusters[key]:
            
            return True
    
    return False
def find_pointer_pairs(found_pointers, temp_dict, current_pair):
    for pair in temp_dict:
        compared_pair = (pair, temp_dict[pair])
        if value_exists_in_pair(current_pair, compared_pair) and compared_pair not in found_pointers:
            
            found_pointers.append(compared_pair)
            find_pointer_pairs(found_pointers, temp_dict, compared_pair)

    return found_pointers
    
def value_exists_in_pair(current_pair, compared_pair):
    
    return current_pair[0] == compared_pair[0] or current_pair[0] == compared_pair[1][0] or current_pair[1][0] == compared_pair[0] or current_pair[1][0] == compared_pair[1][0]

def get_values_of_attribute(strucute_att_dict, attribute):
    values = []
    for struct_object in strucute_att_dict[attribute]:
        temp_pairs = struct_object.get_key_value_pairs()
        for pair in temp_pairs:
            if pair[0] == attribute:
                values.append(pair[1])

    return values
def create_cluster_sets(clusters):
    cluster_sets = {}
    for key in clusters:
        temp_array = []
        array_of_pairs = clusters[key]
        if(len(array_of_pairs) > 0):
            for pair in array_of_pairs:
                temp_array.append(pair[0])
                temp_array.append(pair[1][0])
            cluster_sets[key] = set(temp_array)
    return cluster_sets


def create_token_blocks(cluster_sets, attribute_dict): 
    token_clusters = {}
    for key in cluster_sets:
        current_cluster_attributes = cluster_sets[key]
        current_block_entities = []
        for attribute in current_cluster_attributes:
            objects_with_attribute = attribute_dict[attribute]
            for temp_object in objects_with_attribute:
                if (type(temp_object) != list):
                    current_value = get_value_of_object(attribute, temp_object)
                    split_value = current_value.split()
                    for part in split_value:

                        if part not in token_clusters:
                            list_of_entities = get_shared_entities(part, attribute_dict, current_block_entities, current_cluster_attributes)
                            token_clusters[part] = list_of_entities
    return token_clusters
def get_shared_entities(split_value, attribute_dict, current_block_entities, current_cluster_attributes):
    found_entities = []
    for attribute in current_cluster_attributes:

        for iterated_object in attribute_dict[attribute]:
            
            if type(iterated_object) != list:
                iterated_object_value = get_value_of_object(attribute, iterated_object)
                
                
                split_token = iterated_object_value.split()
                
                for split_part in split_token:

                    
                    if split_part == split_value:

                        found_entities.append(iterated_object)
    return found_entities

def get_value_of_object(attribute, temp_object):
    for key_value_pair in temp_object.get_key_value_pairs():
        if key_value_pair[0] == attribute:
            return key_value_pair[1]
    return ""


def merge_dicts(dict1, dict2):
    for key in dict2:
        if(key in dict1 and len(dict1[key]) > 0):
            dict1[key].append(dict2[key])
        else:
            dict1[key] = dict2[key]
    return dict1
def remove_useless_blocks(token_blocks):
    useless_blocks = []
    for key in token_blocks:
        if len(token_blocks[key]) == 1:
            useless_blocks.append(key)

    for key in useless_blocks:
        del token_blocks[key]


def main():
    
    structure_list = open_csv("structure_data.csv")
    structure_list_2 = open_csv("structure_data_2.csv")
    
    structure_att_dict = objects_to_dict(structure_list)
    structure_att_dict_2 = objects_to_dict(structure_list_2)
    #find the most similar attribute pairs between the entities
    similarity_dict = find_similar_attribute(structure_att_dict, structure_att_dict_2)
    print("old lens", len(structure_att_dict), len(structure_att_dict_2))
    #compute clusters based on transitive closure of the attribute pairs
    clusters = transitional_closure_clustering(similarity_dict)
    merged_dict = merge_dicts(structure_att_dict, structure_att_dict_2)
    print("new len", len(merged_dict))
    cluster_sets = create_cluster_sets(clusters)
    token_blocks = create_token_blocks(cluster_sets, merged_dict)
    #this is a tuple, 0 is nodes and 1 edges
    blocking_graph = create_blocking_graph(token_blocks) 
    print(len(blocking_graph[0]), len(blocking_graph[1]))
if __name__ == "__main__":
    main()


