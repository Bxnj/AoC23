import util as ut
import sys
import faulthandler
faulthandler.enable()
sys.setrecursionlimit(15000)

with open('input.txt') as my_file:
    inputArray = my_file.readlines()
sums = []

for k in range(0, len(inputArray)):
    sums.append(0)
    inputArray[k] = inputArray[k].replace("\n", "")

def allPerm(listStrings):
    toDo = []
    done = []
    for strings in listStrings:
        newStrs = getPermutations(strings)
        if "?" not in newStrs[0]:
            done.append(newStrs[0])
            done.append(newStrs[1])
        else:
            toDo.append(newStrs[0])
            toDo.append(newStrs[1])
    if len(toDo) != 0:
        for strings in allPerm(toDo):
            done.append(strings)
    return done


def getPermutations(string2):
    temp = []
    for i in range(0, len(string2)):
        if string2[i] == "?":
            newStr1 = string2[:i] + "." + string2[i + 1:]
            newStr2 = string2[:i] + "#" + string2[i + 1:]
            temp.append(newStr1)
            temp.append(newStr2)
            return temp
    temp.append(string2)
    return temp
def nrOfSolutions(string1):
    nr = 0
    nrBackups = string1.split(" ")[1].split(",")
    for i in range(0, len(nrBackups)):
        nrBackups[i] = int(nrBackups[i])
    if sum(nrBackups) == string1.count("#") + string1.count("?"):
        return 1
    lS = []
    lS.append(string1.split(" ")[0])
    allVariantes = allPerm(lS)
    for var in allVariantes:
        splits = var.split(".")
        while "" in splits:
            splits.remove("")
        te = []
        for i in splits:
            te.append(len(i))
        if te == nrBackups:
            nr += 1
    #print(string1)
    #print(allVariantes)


    return nr

for k in range(0, len(inputArray)):
    sums[k] = nrOfSolutions(inputArray[k])

print(sums)
print(inputArray)
print(sum(sums))
