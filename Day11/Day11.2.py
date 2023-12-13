import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()
factor = 999999

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

toExpandHorizont = []
co = -1
for k in inputArray:
    co+=1
    if set(k) == {"."}:
        toExpandHorizont.append(co)

c = 0
emtpyString = ("")
for i in range(0, len(inputArray[0])):
    emtpyString += "."



toExpandVert = []
for k in range(0,len(inputArray[0])):
    tr = True
    for l in range(0, len(inputArray)):
        if inputArray[l][k] != ".":
            tr = False
    if tr:
        toExpandVert.append(k)

universes = []
copy = []
for i in range(0,len(inputArray)):
    for j in range(0, len(inputArray[i])):
        if inputArray[i][j] == "#":
            universes.append((i,j))
for un in universes:
    copy.append((0,0))
print(copy)
for hor in toExpandHorizont:
    for i in range(0, len(universes)):
        if universes[i][0] > hor:
            copy[i]= (copy[i][0]+factor, copy[i][1])
for hor in toExpandVert:
    for i in range(0, len(universes)):
        if universes[i][1] > hor:
            copy[i]= (copy[i][0], copy[i][1]+factor)
sum = 0

for k in range(0, len(universes)):
    universes[k] = (universes[k][0] + copy[k][0], universes[k][1])
    universes[k] = (universes[k][0], universes[k][1] + copy[k][1])


while len(universes)!=0:
    currentCoord = universes.pop()
    for other in universes:
        sum += max(currentCoord[0], other[0]) - min(currentCoord[0], other[0]) + max(currentCoord[1], other[1]) - min(currentCoord[1], other[1])
print(sum)
