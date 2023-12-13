import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "").split(" ")
    for i in range(0, len(inputArray[k])):
        inputArray[k][i] = int(inputArray[k][i])

print(inputArray)

def diffArr(arr):
    res = []
    for i in range(0, len(arr)-1):
        res.append(arr[i+1]-arr[i])
    return res

sums = []
for k in range(0, len(inputArray)):
    currentArr = inputArray[k]
    subArr = []
    while(set(currentArr) != {0}):
        subArr.append(currentArr[len(currentArr)-1])
        currentArr = diffArr(currentArr)

    print(subArr)
    sums.append((sum(subArr)))
print(sum(sums))