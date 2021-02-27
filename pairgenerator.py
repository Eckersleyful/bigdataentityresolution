import csv
import random 
import os
path = "F:/VSCodeDirs/bigdataentityresolution"
os.chdir(path)

possible_location_attribute = ["breed", "dog_breed", "type"]
possible_location_names = ["Affenpinscher",
      "Afghan Hound",
      "Aidi",
      "Airedale Terrier",
      "Akbash Dog",
      "Akita",
      "Alano Español",
      "Alaskan Klee Kai",
      "Alaskan Malamute",
      "Alpine Dachsbracke",
      "Alpine Spaniel",
      "American Bulldog",
      "American Cocker Spaniel",
      "American Eskimo Dog",
      "American Foxhound",
      "American Hairless Terrier",
      "American Pit Bull Terrier",
      "American Staffordshire Terrier",
      "American Water Spaniel",
      "Anglo-Français de Petite Vénerie",
      "Appenzeller Sennenhund",
      "Ariege Pointer",
      "Ariegeois",
      "Armant",
      "Armenian Gampr dog",
      "Artois Hound",
      "Australian Cattle Dog",
      "Australian Kelpie",
      "Australian Shepherd",
      "Australian Silky Terrier",
      "Australian Stumpy Tail Cattle Dog",
      "Australian Terrier",
      "Azawakh",
      "Bakharwal Dog",
      "Barbet",
      "Basenji",
      "Basque Shepherd Dog",
      "Basset Artésien Normand",
      "Basset Bleu de Gascogne",
      "Basset Fauve de Bretagne",
      "Basset Hound",
      "Bavarian Mountain Hound",
      "Beagle",
      "Beagle-Harrier",
      "Bearded Collie",
      "Beauceron",
      "Bedlington Terrier",
      "Belgian Shepherd Dog (Groenendael)",
      "Belgian Shepherd Dog (Laekenois)",
      "Belgian Shepherd Dog (Malinois)",
      "Bergamasco Shepherd",
      "Berger Blanc Suisse",
      "Berger Picard",
      "Berner Laufhund",
      "Bernese Mountain Dog",
      "Billy"]


possible_constructed_attribute = ["size", "breed_size", "weight", "build_type"]
possible_years = ["large", "medium", "heavy", "small"]

possible_structure_attribute = ["breed_friendliness", "friendliness", "breed_personality"]
possible_structure_name = ["kind", "independent", "friendly", "happy", "social"]

with open('animal_data.csv', 'w', newline = '\n') as new_file:
    writer = csv.writer(new_file, delimiter = ';')

    for x in range(0, 150):
        
        location_pair = random.choice(possible_location_attribute) + "," + random.choice(possible_location_names)
        construction_pair = random.choice(possible_constructed_attribute) + "," + random.choice(possible_years)
        structure_pair = random.choice(possible_structure_attribute) + "," + random.choice(possible_structure_name)
        writer.writerow([location_pair, construction_pair, structure_pair])