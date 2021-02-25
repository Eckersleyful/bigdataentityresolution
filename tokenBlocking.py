import csv

# A class for stuctures of the structure_data.csv, and animals of the animal_data.csv
class Structure:
  def __init__(self, location,constructed,name):
    self.location = location
    self.constructed = constructed
    self.name = name

class Animal:
  def __init__(self, breed,size,personality):
    self.breed = breed
    self.size = size
    self.personality = personality

# For printing the dictionary
def printDict(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            print ("-----------------------------------\n"+k+":")
            printDict(v)
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, Structure):
                print (v.location+", "+v.constructed+", "+v.name)
            elif isinstance(v, Animal):
                print (v.breed+", "+v.size+", "+v.personality)
    else:
        print (obj)

# Get the data from csv file and save it into dictionary.
def csvToDict(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        line_count = 0
        myDict = dict()
        for row in csv_reader:
            for value in row:
                value = value.split(',')[1]
                if file == 'structure_data.csv':
                    structure = Structure(row[0].split(',')[1], row[1].split(',')[1], row[2].split(',')[1])
                    if value in myDict:
                        myDict[value].append(structure)
                    else:
                        myDict[value] = [structure]
                elif file == 'animal_data.csv':
                    animal = Animal(row[0].split(',')[1], row[1].split(',')[1], row[2].split(',')[1])
                    if value in myDict:
                        myDict[value].append(animal)
                    else:
                        myDict[value] = [animal]
            line_count += 1
        

    # Return a list of keys that have only 1 value
    remove_list = []
    for key, value in myDict.items():
        if len(list(filter(bool, value))) == 1:
            remove_list.append(key)
    
    # Remove all the keys with only 1 value
    [myDict.pop(key) for key in remove_list]

    return myDict

myDict = csvToDict("animal_data.csv")


printDict(myDict)

#print(myDict["Male"][0].car)