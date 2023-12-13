with open('florian.txt') as my_file:
    inputArray = my_file.readlines()
print(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
print(inputArray)

def isSymbol(x,y, Arr):
    if Arr[x][y]!="." and Arr[x][y].isdigit()== False:
        return True
    else:
        return False
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
                truth1 = False
                for u in range(-1, numberlength+1):
                    if x>0 and y+u >= 0 and u+y < len(inputArray[0]):
                        if isSymbol(x-1,u+y,inputArray) :
                            truth1 = True
                    if x<len(inputArray)-1 and y+u >= 0 and u+y < len(inputArray[0]):
                        if isSymbol(x+1,u+y,inputArray):
                            truth1 = True

                ## checking sides
                truth2 = False
                if y-1>= 0:
                    if isSymbol(x, y - 1, inputArray):
                        truth2 = True
                if numberlength + y < len(inputArray[0]):
                    if isSymbol(x, y + numberlength, inputArray):
                        truth2 = True
                if truth2 or truth1:
                    sol.append(var)
print(sol)
resulut = 0
for l in range(0, len(sol)):
    resulut += sol[l]

print(resulut)
