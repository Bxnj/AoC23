import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

for k in inputArray:
    print(k)
#print(inputArray)


def rollNorth(arr):
    for k in range(0, len(arr)):
        for x in range(len(arr[len(arr)-k-1])):
            if len(arr)-k-1 != 0:
                if arr[len(arr)-k-1][x] == "O" and arr[len(arr)-k-2][x] == ".":
                    newString1 = arr[len(arr)-k-1][:x] + "." + arr[len(arr)-k-1][x + 1:]
                    newString2 = arr[len(arr)-k-2][:x] + "O" + arr[len(arr)-k-2][x + 1:]
                    arr[len(arr)-k-1] = newString1
                    arr[len(arr)-k-2] = newString2
    return arr


newArr = rollNorth(inputArray)
for i in range(0,len(inputArray)):
    newArr = rollNorth(newArr)
    print(newArr)
for k in newArr:
    print(k)
sol = []
for i in range(len(newArr)):
    cost = len(newArr)-i
    for char in newArr[i]:
        if char == "O":
            sol.append(cost)
print(sum(sol))