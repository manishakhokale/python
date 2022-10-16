print("Demonstration of Dictionary")

Batches = {"PPA": 18000, "LB": 16700, "Python": 16500, "Angular": 15000}

print("data of dictionary:", Batches)

print("data traversal using for loop")
for x in Batches:
    print(x)

print("data traversal using for loop")
for x in Batches:
    print(x,Batches[x])
print()
print("data traversal using for loop")
for x in Batches:
    print(x,Batches.get(x))

keyBatches = Batches.keys()
print(keyBatches)
print(type(keyBatches))
valueBatches = Batches.values()
print(valueBatches)
print(type(valueBatches))

for i in range(0,len(Batches)):
    print("Batch name is:",keyBatches[i],end=" ")
    print("fee are:",valueBatches[i])