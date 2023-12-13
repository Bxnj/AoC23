import util as ut
import numpy as np


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

def findHorizontal(arr):
    prev = ""
    counter = -1
    for line in arr:

        counter += 1
        if line == prev:
            t = True
            for i in range(min(counter, len(arr)-counter)):
                if arr[counter+i] != arr[counter-i-1]:
                    t = False
            if t:
                return counter
        else:
            prev = line
    return -1

#print(inputArray)

def rotate(arr):
    #print("INPUTARRAY:")
    #for k in arr:
    #    print(k)
    result= []
    for i in zip(*arr):
        result.append("".join(i)[::-1])
    #print("Output:")
    #for k in result:
    #    print(k)
    return result
sol = []
newArr = []
for line in inputArray:
    if line == "":

        horz = findHorizontal(newArr)*100
        if horz != -100:
            sol.append(horz)
        else:
        #print()

            result = rotate(newArr)
            vert = findHorizontal(result)
            if vert != -1:
                sol.append(vert)
        newArr = []

    else:
        newArr.append(line)

horz = findHorizontal(newArr)*100
if horz != -100:
    sol.append(horz)
else:
#print()
    result = rotate(newArr)
    vert = findHorizontal(result)
    if vert != -1:
        sol.append(vert)
print(sol)
print(sum(sol))