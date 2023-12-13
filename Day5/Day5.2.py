import time
start_proc = time.process_time()
with open('message.txt') as my_file:
    inputArray = my_file.readlines()
##(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
##print(inputArray)


def mapping(initialRanges, mapFunc):
    result = []
    if len(mapFunc) == 0:
        return initialRanges

    noTake = []
    for e in range(0, len(mapFunc)):
        #print(e)
        destStart = mapFunc[e][0]
        sourceStart = mapFunc[e][1]
        rng = mapFunc[e][2]
        lookedAt=[]
        for l in range(0, len(initialRanges)):
            #print(initialRanges)
            #print(mapFunc[e])
            temp=[]
            diff = destStart - sourceStart
            if sourceStart <= initialRanges[l][0] and sourceStart+rng >= initialRanges[l][1]:
                temp=[initialRanges[l][0]+diff,initialRanges[l][1] + diff]
                result.append(temp)
                noTake.append(initialRanges[l])
                #print("NOTAKE" + str(noTake))
            elif sourceStart >= initialRanges[l][0] and sourceStart+rng <= initialRanges[l][1]:
                temp = [destStart, destStart+rng]
                result.append(temp)
                initialRanges.append([sourceStart + rng +1, initialRanges[l][1]])
                initialRanges[l][1] = sourceStart-1

            elif sourceStart <= initialRanges[l][0] and sourceStart+rng <= initialRanges[l][1] and sourceStart+rng >= initialRanges[l][0]:
                temp = [initialRanges[l][0]+diff, destStart+rng]
                initialRanges[l][0] = sourceStart+rng-1
                result.append(temp)
            elif sourceStart >= initialRanges[l][0] and sourceStart+rng >= initialRanges[l][1] and sourceStart <= initialRanges[l][1]:
                temp = [destStart, destStart+(initialRanges[l][1]-sourceStart)]
                result.append(temp)
                initialRanges[l][1] = sourceStart-1
    for i in range(0, len(initialRanges)):
        if initialRanges[i] not in noTake:
            result.append(initialRanges[i])
    return result

seeds = inputArray[0].split(" ")
seed = []
doneRanges = []
for i in range(len(seeds)):
    if i != 0 and i%2 == 0:
        nr1 = int(seeds[i-1])
        nr2 = nr1+int(seeds[i])
        doneRanges.append([nr1, nr2])

#print(doneRanges)


def compressoverlap(ranges):
    solution = []
    #print("INPUT: " + str(ranges))
    if len(ranges) == 0:
        return ranges

    for i in range(len(ranges)):
        if solution == []:
            solution.append(ranges[i])
        else:
            lad = False
            for k in range(0, len(solution)):
                if solution[k][0] >= ranges[i][0] and solution[k][0] <= ranges[i][1]:
                    #print("1")
                    solution[k] = ranges[i]
                    lad = True
                elif solution[k][0] >= ranges[i][0] and solution[k][0] <= ranges[i][1] and solution[k][1] >= ranges[i][1]:
                    #print("3")
                    solution[k][0] = ranges[i][0]
                    lad = True
                elif solution[k][0] <= ranges[i][0] and solution[k][1] <= ranges[i][1] and solution[k][1] >= ranges[i][0]:
                    #print("4")
                    solution[k][1] = ranges[i][1]
                    lad = True
                elif solution[k][1] == ranges[i][0] or solution[k][1] == ranges[i][0]+1:
                    solution[k][1] = ranges[i][1]
                elif solution[k][0] == ranges[i][1] or solution[k][0] == ranges[i][1]+1:
                    solution[k][0] = ranges[i][0]
            if not lad:
                #print("ADDING" + str(ranges[i]))
                solution.append(ranges[i])


    #print("SOLUTION: " + str(solution))
    return solution



print("NEW")
initialRanges = doneRanges
print(initialRanges)
tru = False
map = []


for j in range(len(inputArray)):
    if j > 0 and not tru:
        if inputArray[j] == "":
            tru = True
        else:
            map.append([int(inputArray[j].split(" ")[0]),int(inputArray[j].split(" ")[1]),int(inputArray[j].split(" ")[2])])
    elif tru:
        #print("Mapping")
        initialRanges = mapping(initialRanges, map)
        #print(initialRanges)
        #print("Compressiion of list length: " + str(len(initialRanges)))
        initialRanges = initialRanges

        #print("Compressed to list length: " + str(len(initialRanges)))
        #print(initialRanges)
        map = []
        tru = False
final = mapping(initialRanges, map)
print(final)
sol = []
for i in range(len(final)):
    if final[i][0] != 0:
        sol.append(final[i][0])
print(sol)
print(min(sol))
end_proc = time.process_time()
print(f'process time: {end_proc-start_proc:5.3f}s')