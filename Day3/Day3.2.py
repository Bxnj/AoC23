with open('florian.txt') as my_file:
    inputArray = my_file.readlines()
print(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
print(inputArray)

def isSymbol(x,y, Arr):
    if Arr[x][y] =="*":
        return True
    else:
        return False

helperList = []
sol = []
for x in range(0, len(inputArray)):
    forbidden = 0
    for y in range(0, len(inputArray[x])):
        forbidden -=1
        if forbidden <= 0:
            if inputArray[x][y].isdigit():

                stringVal = ""
                for i in range(y, len(inputArray[x])):
                    if inputArray[x][i].isdigit():
                        stringVal += inputArray[x][i]
                    else:
                        break

                var = int(stringVal)
                numberlength = len(stringVal)
                forbidden = numberlength

                ##checking top:

                for u in range(-1, numberlength+1):
                    if x>0 and y+u >= 0 and u+y < len(inputArray[0]):
                        if isSymbol(x-1,u+y,inputArray) :
                            helperList.append([var,x-1,u+y])
                    if x<len(inputArray)-1 and y+u >= 0 and u+y < len(inputArray[0]):
                        if isSymbol(x+1,u+y,inputArray):
                            helperList.append([var,x+1,u+y])

                ## checking sides

                if y-1>= 0:
                    if isSymbol(x, y - 1, inputArray):
                        helperList.append([var,x,y-1])
                if numberlength + y < len(inputArray[0]):
                    if isSymbol(x, y + numberlength, inputArray):
                        helperList.append([var,x,y+numberlength])
donex= []
doney=[]
print(sol)
x=0
y=0
ignore = []
resulut = 0
print(helperList)


final = []
help2 = []
done = []
for i in range(0,len(helperList)):
    val1 = helperList[i][0]
    x1 = helperList[i][1]
    y1 = helperList[i][2]
    tempCoord = -1

    count = 0
    for l in range(0,len(helperList)):
        if helperList[l][1] == x1 and helperList[l][2] == y1 and l not in done:
            count += 1
            tempCoord = l
            done.append(l)

    if count != 2:
        tempCoord = -1

    if tempCoord != -1:
        final.append(val1*helperList[tempCoord][0])
printer = 0
for q in range(0, len(final)):
    printer += final[q]

print(printer)