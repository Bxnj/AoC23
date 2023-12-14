import util as ut
import sys
from functools import cache
import faulthandler
faulthandler.enable()
sys.setrecursionlimit(15000)
import time


with open('input.txt') as my_file:
    inputArray = my_file.readlines()
sums = []

for k in range(0, len(inputArray)):
    sums.append(0)
    inputArray[k] = inputArray[k].replace("\n", "")


for i in range(0, len(inputArray)):
   front = inputArray[i].split(" ")[0]
   back = inputArray[i].split(" ")[1]
   inputArray[i] = front+"?"+front+"?"+front+"?"+front+"?"+front+" " + back + ","+ back + ","+ back + ","+ back + ","+ back


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
    print(string1)
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
dp = {}





#for k in range(0, len(inputArray)):
#    print("DOING LINE: " + str(k))
#    nrs = inputArray[k].split(" ")[1].split(",")
#    for t in range(0, len(nrs)):
#        nrs[t] = int(nrs[t])
#    print("Numbers: "+ str(nrs))

#    intervals = inputArray[k].split(" ")[0].split(".")
#    while "" in intervals:
#        intervals.remove("")
#    print("Intervals: " + str(intervals))

#    for inter in intervals:
#        tem = []
#        for leng in nrs:
#            if sum(tem)+leng<= len(inter):
#                tem.append(leng)
#            else:
#                break
#        print(tem)

@cache
def myLovelyrec(uniqueid, stri, curInd , indexOfCurGr, amDmgSp, setNext = False, setNextDmg = False):
    if curInd == len(stri):
        if (amDmgSp == 0 and indexOfCurGr == len(groups)) or (indexOfCurGr == len(groups) - 1 and amDmgSp == groups[indexOfCurGr]):
            return 1
        else:
            return 0
    chara = stri[curInd]
    if not setNext and chara == "?":
        return myLovelyrec(uniqueid, stri, curInd, indexOfCurGr, amDmgSp, True, True) + myLovelyrec(uniqueid, stri, curInd, indexOfCurGr, amDmgSp, True, False)
    elif setNextDmg or chara == "#":
        return myLovelyrec(uniqueid, stri, curInd + 1, indexOfCurGr, amDmgSp + 1)
    else:
        if amDmgSp != 0:
            if indexOfCurGr < len(groups) and amDmgSp == groups[indexOfCurGr]:
                return myLovelyrec(uniqueid, stri, curInd + 1, indexOfCurGr + 1, 0)
            else:
                return 0
        else:
            return myLovelyrec(uniqueid, stri, curInd + 1, indexOfCurGr, 0)
solu = []
for k in range(0, len(inputArray)):
    start_time = time.time()

    print("DOING LINE: " + str(k))
    nrs = inputArray[k].split(" ")[1].split(",")
    for t in range(0, len(nrs)):
        nrs[t] = int(nrs[t])
    #print("Numbers: "+ str(nrs))

    intervals = inputArray[k].split(" ")[0]
    groups = nrs
    #print(intervals)
    w = myLovelyrec(k,intervals, 0, 0, 0)
    solu.append(w)
    #print("Output for every line: " + str(w))
    print("Finished Line: " + str(k) + " in --- %s seconds ---" % (time.time() - start_time))
print(solu)
for o in solu:
    print(o)
print(sum(solu))

