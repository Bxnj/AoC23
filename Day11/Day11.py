import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

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
for i in toExpandHorizont:
    inputArray.insert(i+c, emtpyString)
    c+=1


toExpandVert = []
for k in range(0,len(inputArray[0])):
    tr = True
    for l in range(0, len(inputArray)):
        if inputArray[l][k] != ".":
            tr = False
    if tr:
        toExpandVert.append(k)

for i in range(0,len(inputArray)):
    st = inputArray[i]
    c = -1
    for k in toExpandVert:
        c+=1
        st = st[:k+c] + '.' + st[k+c:]
    inputArray[i] = st

universes = []
for i in range(0,len(inputArray)):
    for j in range(0, len(inputArray[i])):
        if inputArray[i][j] == "#":
            universes.append((i,j))
sum = 0
while len(universes)!=0:
    currentCoord = universes.pop()
    for other in universes:
        sum += max(currentCoord[0], other[0]) - min(currentCoord[0], other[0]) + max(currentCoord[1], other[1]) - min(currentCoord[1], other[1])
print(sum)