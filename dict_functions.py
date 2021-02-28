def objects_to_dict(object_list):
    new_dict = {}
    for structure in object_list:
        attribute_pairs = structure.get_key_value_pairs()
        for attribute_pair in attribute_pairs:
         
            check_key(new_dict, attribute_pair[0], structure)
    
    return new_dict
def check_key(check_dict, new_key, structure):
        
    if new_key in check_dict:
        check_dict[new_key].append(structure)
    else:
        check_dict[new_key] = [structure]