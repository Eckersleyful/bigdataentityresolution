CURRENT_WORKING_DIR = "F:/VSCodeDirs/bigdataentityresolution/"
import csv
from structure import Structure
def open_csv(file_name):
    lines = []
    list_of_objects = []
    with open(CURRENT_WORKING_DIR + file_name, 'r', encoding='utf-8-sig') as new_file:
        reader = csv.reader(new_file, delimiter = ";")
        line_index = 0
        for line in reader:
            line_index += 1
            if line not in lines:
                lines.append(line)
                key_value_pairs = []
                for element in line:
                    temp = element.split(",")
                    key_value_pairs.append((temp[0], temp[1]))
                create_structure_objects(key_value_pairs, list_of_objects)
    return list_of_objects


def create_structure_objects(line, into_list):

    into_list.append(Structure(line))