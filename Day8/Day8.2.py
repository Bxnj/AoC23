import util as ut
from math import lcm



with open('message.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

instructions = inputArray[0]
inputArray.remove(inputArray[0])
#print(inputArray)

allNodes = []

class Node:
    def __init__(self, own, left, right):
        self.own = own
        self.left = left
        self.right = right

def isNode(nodeList, id):
    for i in range(0, len(nodeList)):
        if nodeList[i].own == id:
            return nodeList[i]

    #def calculate_area(self):
    #    return round(math.pi * self.radius ** 2, 2)
inputArray.remove("")

def winCheck(node):
    check = False
    if node.own[2] == "Z":
        check = True
    return check

for i in range(0,len(inputArray)):
    equalSplit = inputArray[i].split(" = ")
    ownID = equalSplit[0]
    split2 = equalSplit[1].split(", ")
    left = split2[0].replace("(", "")
    right = split2[1].replace(")", "")
    newNode = Node(ownID,left,right)
    allNodes.append(newNode)


for i in range(0, len(allNodes)):
    allNodes[i].left = isNode(allNodes, allNodes[i].left)
    allNodes[i].right = isNode(allNodes, allNodes[i].right)

counter = 0
currentNodes = []
for i in range(0, len(allNodes)):
    #print(allNodes[i].own[2])
    if allNodes[i].own[2] == "A":
        currentNodes.append(allNodes[i])

list = []
for l in range(len(currentNodes)):
    x = 0
    counter = 0
    while x == 0:
        for char in instructions:
            counter += 1
            if char == "L":
                currentNodes[l] = currentNodes[l].left
            elif char == "R":
                currentNodes[l] = currentNodes[l].right
            else:
                print("SHIT")
            if winCheck(currentNodes[l]) and x == 0:
                x += 1
                print(counter)
                list.append(counter)
                break


print(list)
#print(str(lcm(list[0],list[3], list[5], list[1])))
print(str(lcm(list[0],list[1],list[2],list[3],list[4],list[5])))






