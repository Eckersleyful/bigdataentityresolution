import tokenBlocking

def jaccard_sim(a, b, c): 
    return float(c / (a + b - c))

# Check if entities e1 and e2 have exactly same attributes.
def isMatch(e1, e2):
    if isinstance(e2, tokenBlocking.Structure):
        if(e1 == e2):
            return True
        else:
            return False
    elif isinstance(e2, tokenBlocking.Animal):
        if(e1 == e2):
            return True
        else:
            return False


# Count in how many blocks of myDict entities 1 and 2 appear, and in how many common blocks they have.
def countBlocks(entity1, entity2, myDict, c1, c2, c3):
    if isinstance(myDict, dict):
        for k, v in myDict.items():
            res = countBlocks(entity1, entity2, v, c1, c2, c3)
            c1 = res[0]
            c2 = res[1]
            c3 = res[2]
    elif isinstance(myDict, list):
        both1 = False
        both2 = False
        for v in myDict:
            if isMatch(v, entity1):
                c1 += 1
                both1 = True
            elif isMatch(v, entity2):
                c2 += 1
                both2 = True 
        if both1 and both2:
            c3 +=1       
    return([c1, c2, c3])
