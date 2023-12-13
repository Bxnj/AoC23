


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

def findHorizontal(arr):
    prev = ""
    counter = -1
    for line in arr:
        counter += 1
        diff = 0
        for letter1, letter2 in zip(line, prev):
            if letter1 != letter2:
                diff += 1
        if line == prev or diff == 1:
            t = True
            diff = 0
            for i in range(min(counter, len(arr)-counter)):

                for letter1, letter2 in zip(arr[counter+i], arr[counter-i-1]):
                    if letter1 != letter2:
                        diff += 1
                if diff > 1:
                    t = False
                    prev = line
            if t and diff == 1:
                return counter
        else:
            prev = line
    return -1


def rotate(arr):
    result= []
    for i in zip(*arr):
        result.append("".join(i)[::-1])
    return result
sol = []
newArr = []
for line in inputArray:

    if line == "":
        print(len(sol))
        horz = findHorizontal(newArr)*100
        if horz != -100:
            sol.append(horz)
        else:
        #print()

            result = rotate(newArr)
            vert = findHorizontal(result)
            if vert != -1:
                sol.append(vert)
            else:
                for k in newArr:
                    print(k)
        newArr = []

    else:
        newArr.append(line)
print("Horizontal")
horz = findHorizontal(newArr)*100
if horz != -100:
    print("TEST")
    sol.append(horz)
else:
    print("Vertical")

    result = rotate(newArr)
    vert = findHorizontal(result)
    print(vert)
    if vert != -1:
        sol.append(vert)
print(sol)
print(sum(sol))