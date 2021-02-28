import csv
import random 
import os
path = "F:/VSCodeDirs/bigdataentityresolution"
os.chdir(path)

possible_location_attribute = ["location", "located", "located at"]
possible_location_names = ['Canary',
'Barnett',
'Vahlen',
'Surrey',
'Delaware',
'Sachs',
'New Castle',
'Marcy',
'Donald',
'School',
'Knutson',
'Petterle',
'South',
'Eastlawn',
'Oxford',
'Schiller',
'Hooker',
'Welch',
'Sachtjen',
'Washington',
'Lakewood Gardens',
'Sugar',
'Hayes',
'Golf Course',
]


possible_constructed_attribute = ["built", "constructed at", "constructed", "construction"]
possible_years = ["1555", "1234", "1000", "0", "972", "875", "1123", "1762", "1918", "1984", "1999"]

possible_structure_attribute = ["building_name", "name", "building"]
possible_structure_name = ["Southern Globe", "Lakeuden risti", "Maj Tahal", "Russian rock", "Very big palace", "Chinese palace", "Huge Castle", "African temple", "Asian thing"]

with open('structure_data.csv', 'w', newline = '\n') as new_file:
    writer = csv.writer(new_file, delimiter = ';')

    for x in range(0, 300):
        
        location_pair = random.choice(possible_location_attribute) + "," + random.choice(possible_location_names)
        construction_pair = random.choice(possible_constructed_attribute) + "," + random.choice(possible_years)
        structure_pair = random.choice(possible_structure_attribute) + "," + random.choice(possible_structure_name)
        writer.writerow([location_pair, construction_pair, structure_pair])