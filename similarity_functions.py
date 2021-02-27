def jaccard(list1, list2):
    set_1 = set(list1)
    set_2 = set(list2)
    intersection = set_1.intersection(set_2)
    return float(len(intersection)) / (len(set_1) + len(set_2) - len(intersection))