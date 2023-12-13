import util as ut


with open('input.txt') as my_file:
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

for i in range(0, len(allNodes)):
    if allNodes[i].own == "AAA":
        currentNode = allNodes[i]
x=0
while x == 0:
    for char in instructions:
        counter += 1
        if char == "L":
            currentNode = currentNode.left
        elif char == "R":
            currentNode = currentNode.right
        else:
            print("SHIT")
        ##print(currentNode.own)
        if currentNode.own == "ZZZ":
            x=1
            break

print(counter)


