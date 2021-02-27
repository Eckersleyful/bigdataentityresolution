import tokenBlocking
import jaccardScheme

myDict = tokenBlocking.csvToDict("structure_data.csv")
#tokenBlocking.printDict(myDict)

c1 = 0
c2 = 0
c3 = 0
res = jaccardScheme.countBlocks(myDict["New Castle"][1], myDict["New Castle"][2], myDict, c1, c2, c3)
print(str(res[0])+" "+str(res[1])+ " " +str(res[2]))

v = myDict["New Castle"][1]
b =  myDict["New Castle"][2]
print (v.location+", "+v.constructed+", "+v.name)
print (b.location+", "+b.constructed+", "+b.name)

jaccard = jaccardScheme.jaccard_sim(res[0], res[1], res[2])
print("Common blocks scheme: "+str(res[2]))
print("Jaccard scheme: "+str(jaccard))
