import util as ut

with open('input.txt') as my_file:
    inputArray = my_file.readlines()
(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")



t = inputArray[0].split("   ")
times = inputArray[0].split(":")[1]
distance = inputArray[1].split(":")[1]


times = int(times.replace(" ", ""))
distance = int(distance.replace(" ", ""))



print(times)
print(distance)


def getWinningNr(time, prevWinner):
    t= 0
    for i in range(time):
        potentialSpeed = i
        distance = i*(time-i)
        if distance > prevWinner:
            t+=1
    return t




final = getWinningNr(times, distance)

print(final)