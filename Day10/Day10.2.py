import util as ut

import sys
import faulthandler
import time
start_proc = time.process_time()
sys.setrecursionlimit(15000)
faulthandler.enable()
with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
biggerArr = []
for i in range(0, len(inputArray)*3):
    temp = []
    for k in range(0, len(inputArray[0])*3):
        temp.append(".")
    biggerArr.append(temp)


def starterCoordsFun(visited, origin, fullArr):
    #fullArr[origin[0]][origin[1]]
    if(origin[0] > 0 and (fullArr[origin[0]-1][origin[1]] == "|" or fullArr[origin[0]-1][origin[1]] == "7" or fullArr[origin[0]-1][origin[1]] == "F")and (origin[0]-1,origin[1]) not in visited):
        return (origin[0]-1, origin[1])
    if (origin[1] < len(fullArr[0]) and (fullArr[origin[0]][origin[1]+1] == "-" or fullArr[origin[0]][origin[1]+1] == "J" or
                           fullArr[origin[0]][origin[1]+1] == "7") and (origin[0], origin[1]+1) not in visited):
        return (origin[0], origin[1]+1)
    if (origin[1] > 0 and (fullArr[origin[0]][origin[1] - 1] == "-" or fullArr[origin[0]][origin[1] - 1] == "L" or
                           fullArr[origin[0]][origin[1] - 1] == "F") and (origin[0], origin[1] - 1) not in visited):
        return (origin[0], origin[1] - 1)
    if (origin[0] < len(fullArr) and (fullArr[origin[0] + 1][origin[1]] == "|" or fullArr[origin[0] + 1][origin[1]] == "L" or
                           fullArr[origin[0] + 1][origin[1]] == "J") and (origin[0] + 1, origin[1]) not in visited):
        return (origin[0] + 1, origin[1])

visited = []
starterCoords = (0,0)
allCoords = []
for k in range(0 , len(inputArray)):
    for i in range(0, len(inputArray[k])):
        if inputArray[k][i] == "S":
            starterCoords = (k,i)
            visited.append(starterCoords)
        else:
            temp = (k,i)
            allCoords.append(temp)
print(len(allCoords))
def getNext(coords, fullArr, visited):
    sym = fullArr[coords[0]][coords[1]]
    if sym == "|":
        ver1 = (coords[0]-1, coords[1])
        ver2 = (coords[0]+1, coords[1])
        if ver1 not in visited:
            return ver1
        else:
            return ver2
    if sym == "-":
        ver1 = (coords[0], coords[1]-1)
        ver2 = (coords[0], coords[1]+1)
        if ver1 not in visited:
            return ver1
        else:
            return ver2
    if sym == "L":
        ver1 = (coords[0]-1, coords[1])
        ver2 = (coords[0], coords[1]+1)
        if ver1 not in visited:
            return ver1
        else:
            return ver2
    if sym == "J":
        ver1 = (coords[0]-1, coords[1])
        ver2 = (coords[0], coords[1]-1)
        if ver1 not in visited:
            return ver1
        else:
            return ver2
    if sym == "7":
        ver1 = (coords[0]+1, coords[1])
        ver2 = (coords[0], coords[1]-1)
        if ver1 not in visited:
            return ver1
        else:
            return ver2
    if sym == "F":
        ver1 = (coords[0]+1, coords[1])
        ver2 = (coords[0], coords[1]+1)
        if ver1 not in visited:
            return ver1
        else:
            return ver2

path1 = starterCoordsFun(visited, starterCoords, inputArray)
allCoords.remove(path1)
visited.append(path1)
path2 = starterCoordsFun(visited, starterCoords, inputArray)
allCoords.remove(path2)
visited.append(path2)

tem1 = path1
tem2 = path2

steps = 1
while path1 != path2 :
    path1 = getNext(path1,inputArray,visited)
    path2 = getNext(path2, inputArray, visited)
    if path1 in visited and path2 in visited:
        break
    if path2 == path1:
        visited.append(path1)
        allCoords.remove(path1)
        steps += 1
        break
    allCoords.remove(path1)
    allCoords.remove(path2)
    visited.append(path1)
    visited.append(path2)

    #print(str(path1) + " and " + str(path2))
    steps+=1
#print(steps)

#print(starterCoords)


def isAroundLoop(totArr, origin, visited):
    toVisit=[]
    sol = []

    toVisit.append(origin)
    while len(toVisit) != 0:
        el = toVisit.pop()
        sol.append(el)
        visited.append(el)
        if el[0] > 0 and (el[0]-1,el[1]) not in visited and (el[0]-1,el[1]) not in toVisit:
            toVisit.append((el[0]-1,el[1]))

        if el[1] > 0 and (el[0], el[1]-1) not in visited and (el[0], el[1]-1) not in toVisit:
            toVisit.append((el[0], el[1]-1))
        if el[0] < len(totArr)-1 and (el[0]+1, el[1]) not in visited and (el[0]+1, el[1]) not in toVisit:
            toVisit.append((el[0]+1, el[1]))
        if el[1] < len(totArr[0])-1 and (el[0], el[1]+1) not in visited and (el[0], el[1]+1) not in toVisit:
            toVisit.append((el[0], el[1]+1))


    return sol
loop = []

for i in visited:
    loop.append(i)
totalOutside = []
for i in range(0,len(inputArray[0])):
    if (0,i) not in visited:
        tempOutSide = isAroundLoop(inputArray, (0,i), visited)
        for e in tempOutSide:
            if e not in totalOutside:
                visited.append(e)
                totalOutside.append(e)
for i in range(0,len(inputArray)):
    if (i,0) not in visited:
        tempOutSide = isAroundLoop(inputArray, (i,0), visited)
        for e in tempOutSide:
            if e not in totalOutside:
                visited.append(e)
                totalOutside.append(e)
for i in range(0,len(inputArray)):
    if (i, len(inputArray[0])-1) not in visited:
        tempOutSide = isAroundLoop(inputArray, (i,len(inputArray[0])-1), visited)
        for e in tempOutSide:
            if e not in totalOutside:
                visited.append(e)
                totalOutside.append(e)
for i in range(0,len(inputArray[0])):
    if (len(inputArray)-1, i) not in visited:
        tempOutSide = isAroundLoop(inputArray, (i,len(inputArray)-1), visited)
        for e in tempOutSide:
            if e not in totalOutside:
                visited.append(e)
                totalOutside.append(e)


#print(outside)


for k in totalOutside:
    if k in allCoords:
        allCoords.remove(k)


def isInside(loop, fullArr, coord):
    left = 0

    for i in range(0,coord[1]):
        if fullArr[coord[0]][i] != "-" and (coord[0], i) in loop:
            left+=1
    right=0
    for i in range(coord[1]+1, len(fullArr[0])):
        if fullArr[coord[0]][i] != "-" and (coord[0], i) in loop:
            right += 1

    up = 0
    for i in range(0, coord[0]):
        if fullArr[i][coord[1]]!= "|" and (i, coord[1]) in loop:
            up += 1

    down = 0
    for i in range(coord[0]+1, len(fullArr)):
        if fullArr[i][coord[1]] != "|" and (i, coord[1]) in loop:
            down += 1

    if down %2 == 0 and up%2==0 and left%2==0 and right%2==0:
        return False
    else:
        return True


if starterCoords[0] == tem1[0] and starterCoords[1] == tem2[1] and starterCoords[1] == tem1[1]-1 and starterCoords[0] == tem2[0]-1:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "F")
if starterCoords[1] == tem1[1] == tem2[1]:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "|")
if starterCoords[0] == tem1[0] == tem2[0]:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "-")
if starterCoords[0] == tem1[0]+1 and starterCoords[1] == tem2[1]-1 and starterCoords[0] == tem2[0] and starterCoords[1] == tem1[1]:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "L")
if starterCoords[0] == tem1[0]+1 and starterCoords[1] == tem2[1]+1 and starterCoords[0] == tem2[0] and starterCoords[1] == tem1[1]:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "J")
if starterCoords[0] == tem1[0] and starterCoords[1] == tem2[1] and starterCoords[1] == tem1[1]+1 and starterCoords[0] == tem2[0]-1:
    inputArray[starterCoords[0]] = inputArray[starterCoords[0]].replace("S", "7")
def setNew(biggerArr,inputArray,coord):
    c0 = coord[0]
    c1 = coord[1]
    if inputArray[c0][c1] == "|":
        biggerArr[c0*3+1][c1*3+1] = "|"
        biggerArr[c0*3+2][c1*3+1] = "|"
        biggerArr[c0*3][c1*3+1] = "|"
    if inputArray[c0][c1] == "-":
        biggerArr[c0*3+1][c1*3+1] = "-"
        biggerArr[c0*3+1][c1*3] = "-"
        biggerArr[c0*3+1][c1*3+2] = "-"
    if inputArray[c0][c1] == "L":
        biggerArr[c0*3+1][c1*3+1] = "L"
        biggerArr[c0*3][c1*3+1] = "|"
        biggerArr[c0*3+1][c1*3+2] = "-"
    if inputArray[c0][c1] == "J":
        biggerArr[c0*3+1][c1*3+1] = "J"
        biggerArr[c0*3][c1*3+1] = "|"
        biggerArr[c0*3+1][c1*3] = "-"
    if inputArray[c0][c1] == "7":
        biggerArr[c0*3+1][c1*3+1] = "7"
        biggerArr[c0*3+2][c1*3+1] = "|"
        biggerArr[c0*3+1][c1*3] = "-"
    if inputArray[c0][c1] == "F":
        biggerArr[c0*3+1][c1*3+1] = "F"
        biggerArr[c0*3+2][c1*3+1] = "|"
        biggerArr[c0*3+1][c1*3+2] = "-"
    if inputArray[c0][c1] == "S":
        biggerArr[c0*3][c1*3] = "S"
        biggerArr[c0*3][c1*3+1] = "S"
        biggerArr[c0*3][c1*3+2] = "S"
        biggerArr[c0 * 3 + 1][c1 * 3] = "S"
        biggerArr[c0 * 3 + 1][c1 * 3 + 1] = "S"
        biggerArr[c0 * 3 + 1][c1 * 3 + 2] = "S"
        biggerArr[c0 * 3 + 2][c1 * 3] = "S"
        biggerArr[c0 * 3 + 2][c1 * 3 + 1] = "S"
        biggerArr[c0 * 3 + 2][c1 * 3 + 2] = "S"


coord1 = -1
for i in inputArray:
    coord1+=1
    coord2 = -1
    for k in i:
        coord2 += 1
        setNew(biggerArr,inputArray,(coord1, coord2))


print("NO")
for k in biggerArr:
    print(k)
#print(starterCoords)
#print(tem1)
#print(tem2)
#print(len(totalOutside))
#print(len(loop))
#print(len(allCoords))
#print(allCoords)
notIn = []



for l in notIn:
    allCoords.remove(l)
#print(allCoords)

biggerAll = []
biggerLoop = []
for i in range(0, len(biggerArr)):
    for j in range(0, len(biggerArr[i])):
        biggerAll.append((i,j))
biggerStarter = (starterCoords[0]*3+1, starterCoords[1]*3+1)
biggerLoop.append(biggerStarter)
biggerPath1 = starterCoordsFun(biggerLoop, biggerStarter, biggerArr)
biggerAll.remove(biggerPath1)
biggerLoop.append(biggerPath1)
biggerPath2 = starterCoordsFun(biggerLoop, biggerStarter, biggerArr)
biggerAll.remove(biggerPath2)
biggerLoop.append(biggerPath2)



steps = 1
print("YES!")
while biggerPath1 != biggerPath2 :
    biggerPath1 = getNext(biggerPath1,biggerArr,biggerLoop)
    biggerPath2 = getNext(biggerPath2, biggerArr, biggerLoop)
    if biggerPath1 in biggerLoop and biggerPath2 in biggerLoop:
        break
    if biggerPath2 == biggerPath1:
        biggerLoop.append(biggerPath1)
        biggerAll.remove(biggerPath1)
        steps += 1
        break
    biggerAll.remove(biggerPath1)
    biggerAll.remove(biggerPath2)
    biggerLoop.append(biggerPath1)
    biggerLoop.append(biggerPath2)

    #print(str(path1) + " and " + str(path2))
    steps+=1

visited = []
for i in biggerLoop:
    visited.append(i)
#print("VISITED: " + str(visited))


tempOutSide = isAroundLoop(biggerArr, (0,0), visited)
for e in tempOutSide:
    visited.append(e)


print("DONE")

for u in tempOutSide:
    if u in biggerAll:
        biggerAll.remove(u)
def isInside2(bigArr, biggerAll, coords):
    c0 = coords[0]
    c1 = coords[1]
    if (c0,c1) not in biggerAll and (c0+1,c1) not in biggerAll and (c0-1,c1) not in biggerAll and(c0,c1+1) not in biggerAll and (c0,c1-1) not in biggerAll:
        return True
    else:
        return False


coun = 0
for i in allCoords:
    if (i[0]*3+1, i[1]*3+1) in biggerAll:
        coun += 1


print(coun)
end_proc = time.process_time()
print(f'process time: {end_proc-start_proc:5.3f}s')