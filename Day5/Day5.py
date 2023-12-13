import util as ut

with open('input.txt') as my_file:
    inputArray = my_file.readlines()
##(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
##print(inputArray)


def mapping(seed1, mapFunc):
    print(seed1)
    newSeeds = []
    for q in range(0, len(seed)):
        newSeeds.append(seed1[q])
    for e in range(0, len(mapFunc)):
        destStart = mapFunc[e][0]
        sourceStart = mapFunc[e][1]
        range1 = mapFunc[e][2]
        for o in range(0, len(seed)):
            if seed1[o] <= sourceStart+range1 and seed1[o] >= sourceStart:
                newSeeds[o] = (seed1[o]-sourceStart)+destStart
    print(mapFunc)

    print(newSeeds)
    if newSeeds != seed1:
        print("SHIT")
    return newSeeds



seeds = inputArray[0].split(" ")
seed = []
for i in range(len(seeds)):
    if i != 0:
        seed.append(int(seeds[i]))
##print(seed)

tru = False
map = []
for j in range(len(inputArray)):
    if j > 0 and not tru:
        if inputArray[j] == "":
            tru = True
        else:
            map.append([int(inputArray[j].split(" ")[0]),int(inputArray[j].split(" ")[1]),int(inputArray[j].split(" ")[2])])
    elif tru:
        seed = mapping(seed, map)
        map = []
        tru = False
final = mapping(seed, map)
print(final)
print(min(final))

