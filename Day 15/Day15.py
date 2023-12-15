import util as ut


with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

newArr = inputArray[0].split(",")
for k in range(0, len(newArr)):
    newArr[k].replace(" ", "")
print(newArr)


startingValue = 0

def hash(StartVal, stri):
    newVal = StartVal
    for char in stri:
        newVal += ord(char)
        newVal = (newVal*17)%256
        print("Character: "+ char +" Order:"+str(ord(char)))
    return newVal
sol =[]
for k in newArr:
    sol.append(hash(startingValue, k))
print(sum(sol))