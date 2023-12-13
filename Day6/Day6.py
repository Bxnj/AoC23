import util as ut

with open('input.txt') as my_file:
    inputArray = my_file.readlines()
(inputArray)

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")



t = inputArray[0].split("   ")
times = inputArray[0].split(" ")
distance = inputArray[1].split(" ")

for e in range(0, len(times)):
    for l in range(0,times[e].count(" ")):
        times[e].replace(" ", "")
    if times[e].isdigit():
        times[e] = int(times[e])
for e in range(0, times.count("")):
    times.remove("")
times.remove("Time:")

for e in range(0, len(distance)):
    for l in range(0,distance[e].count(" ")):
        distance[e].replace(" ", "")
    if distance[e].isdigit():
        distance[e] = int(distance[e])
for e in range(0, distance.count("")):
    distance.remove("")

distance.remove("Distance:")

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

sol = []
for l in range(len(times)):
    nr = getWinningNr(times[l], distance[l])
    sol.append(nr)

final = 1
for e in range(len(sol)):
    final = final*sol[e]
print(final)