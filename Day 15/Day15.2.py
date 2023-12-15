import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

newArr = inputArray[0].split(",")
for k in range(0, len(newArr)):
    newArr[k].replace(" ", "")


startingValue = 0
boxes = []
for i in range(0,256):
    boxes.append([])
def hash(StartVal, stri):
    newVal = StartVal
    for char in stri:
        newVal += ord(char)
        newVal = (newVal*17)%256
    return newVal


for k in newArr:
    if "-" in k:
        k=k[:-1]
        hashVal = hash(startingValue, k)
        for i in boxes[hashVal]:
            if i[0] == k:
                temp = i[1]
                boxes[hashVal].remove((k,temp))
    else:
        ind = k.find("=")
        focalLength = k[ind+1:]
        k = k[:-(len(k)-ind)]
        hashVal = hash(startingValue, k)
        t = False
        index = 0
        for i in boxes[hashVal]:
                if i[0] == k:
                    boxes[hashVal][index] = (k,focalLength)
                    t = True
                index += 1
        if not t:
            boxes[hashVal].append((k, focalLength))



sol =[]
for nr in range(0,len(boxes)):
    box = boxes[nr]
    for k in range(0, len(box)):
        val = int(box[k][1])*(k+1)*(nr+1)
        sol.append(val)

print(sum(sol))

