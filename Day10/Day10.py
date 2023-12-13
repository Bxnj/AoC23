import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

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
for k in range(0 , len(inputArray)):
    for i in range(0, len(inputArray[k])):
        if inputArray[k][i] == "S":
            starterCoords = (k,i)
            visited.append(starterCoords)

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
visited.append(path1)
path2 = starterCoordsFun(visited, starterCoords, inputArray)
visited.append(path2)
nr12 = getNext(path1,inputArray,visited)
steps = 1
while path1 != path2:
    path1 = getNext(path1,inputArray,visited)
    visited.append(path1)
    path2 = getNext(path2, inputArray, visited)
    visited.append(path2)
    steps+=1
print(steps)


print(path1)
print(path2)
print(nr12)
print(inputArray)
print(starterCoords)
