import util as ut
from functools import cache

with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")


#print(inputArray)
allBalls = []
blocks = []


for k in range(0, len(inputArray)):
    temp = []
    temp2 = []
    for x in range(0, len(inputArray[k])):
        if inputArray[k][x] == "#":
            temp.append(x)
        if inputArray[k][x] == "O":
            temp2.append(x)
    allBalls.append(temp2)
    blocks.append(temp)
#print(blocks)
#print(allBalls)
def rollWest():
    for i in range(len(blocks)):
        allBlocks = blocks[i]
        currentBalls = allBalls[i]
        lastBlock = -1
        for block in allBlocks:
            for o in range(len(currentBalls)):
                if currentBalls[o] < block and currentBalls[o] >lastBlock:
                    cntr = 1
                    while lastBlock+cntr < block:
                        if lastBlock+cntr not in currentBalls or cntr+lastBlock == currentBalls[o]:
                            currentBalls[o] = lastBlock+cntr
                            break
                        else:
                            cntr+=1

            lastBlock = block
        for o in range(len(currentBalls)):
            if currentBalls[o] > lastBlock:
                cntr = 1
                while True:
                    if lastBlock + cntr not in currentBalls or cntr + lastBlock == currentBalls[o]:
                        currentBalls[o] = lastBlock + cntr
                        break
                    else:
                        cntr += 1
        allBalls[i] = currentBalls


def rollEast():
    for i in range(len(blocks)):
        allBlocks = blocks[i]
        currentBalls = allBalls[i]
        lastBlock = -1
        for block in allBlocks:
            for o in range(len(currentBalls)):
                if currentBalls[o] < block and currentBalls[o] >lastBlock:
                    cntr = 1
                    while block-cntr > lastBlock:
                        if block-cntr not in currentBalls or block-cntr == currentBalls[o]:
                            currentBalls[o] = block-cntr
                            break
                        else:
                            cntr+=1

            lastBlock = block
        for o in range(len(currentBalls)):
            if currentBalls[o] > lastBlock:
                cntr = 1
                while True:
                    if len(inputArray[0])-cntr not in currentBalls or len(inputArray[0])-cntr == currentBalls[o]:
                        currentBalls[o] = len(inputArray[0])-cntr
                        break
                    else:
                        cntr += 1
        allBalls[i] = currentBalls


def rotate():
    new = []
    new2 = []
    for i in range(len(allBalls)):
        new.append([])
        new2.append([])
    for k in range(len(allBalls)):
        for balls in allBalls[k]:
            new[balls].append(k)
        for block in blocks[k]:
            new2[block].append(k)
    return new,new2


#print("HERE")
#print(allBalls)


#print(allBalls)
cycleDP = []
new =[[]]
while new not in cycleDP:
    cycleDP.append(new)

    new = rotate()
    allBalls = new[0]
    blocks = new[1]
    allBalls.reverse()
    blocks.reverse()
    rollWest()
    new = rotate()
    allBalls = new[0]
    blocks = new[1]
    allBalls.reverse()
    blocks.reverse()
    rollEast()
    new = rotate()
    allBalls = new[0]
    blocks = new[1]
    allBalls.reverse()
    blocks.reverse()
    rollWest()
    new = rotate()
    allBalls = new[0]
    blocks = new[1]
    allBalls.reverse()
    blocks.reverse()
    rollEast()
    new = allBalls

coolIndex = cycleDP.index(new)
rest = (1000000000-coolIndex)%(len(cycleDP)-coolIndex)
allBalls = []
blocks = []
print(rest)
print(coolIndex)
print(len(cycleDP)-coolIndex)

for k in range(0, len(inputArray)):
    temp = []
    temp2 = []
    for x in range(0, len(inputArray[k])):
        if inputArray[k][x] == "#":
            temp.append(x)
        if inputArray[k][x] == "O":
            temp2.append(x)
    allBalls.append(temp2)
    blocks.append(temp)





allBalls = cycleDP[rest+coolIndex]
sol = []
for i in range(len(allBalls)):
    cost = len(allBalls)-i
    sol.append(cost*len(allBalls[i]))
print(sum(sol))