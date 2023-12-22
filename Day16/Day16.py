import util as ut




allBeams = []
touchedCoords = []

class Beam():
    def __init__(self, x, y, nextX, nextY):
        self.nextX = nextX
        self.nextY = nextY
        self.x = x
        self.y = y

    def itarate(self, newX, newY):
        print("TESTi")
        print(self.x, self.y)
        itX = self.nextX
        itY = self.nextY
        self.y = itY
        self.x = itX
        self.nextX = newX
        self.nextY = newY
        print(self.x, self.y)
        newCoords = [newX, newY]
        if newCoords not in touchedCoords:
            touchedCoords.append(newCoords)

with open('test.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

newBeam = Beam(0,-1,0,0)
allBeams.append(newBeam)
x = 10
#while len(allBeams) != 0:
while x > 0:
    #print(allBeams)
    x -= 1
    toAppend = []
    print("ONJE")
    for beam in allBeams:
        print(beam.x, beam.y)
        print(beam.nextX, beam.nextY)
        if (beam.nextX < len(inputArray[0]) and beam.nextX >= 0) and (beam.nextY < len(inputArray) and beam.nextY >= 0):
            if inputArray[beam.nextY][beam.nextX] == ".":
                beam.itarate(beam.nextX+(beam.nextX-beam.x),beam.nextY+(beam.nextY-beam.y))
            elif inputArray[beam.nextY][beam.nextX] == "/":
                beam.itarate(beam.nextX, beam.nextY-1)
            elif inputArray[beam.nextY][beam.nextX] == "\\":
                beam.itarate(beam.nextX, beam.nextY + 1)
            elif inputArray[beam.nextY][beam.nextX] == "|":
                if beam.nextY == beam.x+1:
                    beam.itarate(beam.nextX+1, beam.nextY)
                elif beam.nextY == beam.x-1:
                    beam.itarate(beam.nextX-1, beam.nextY)
                else:
                    print("TEST")
                    beam.itarate(beam.nextX, beam.nextY - 1)
                    newBeam = Beam(beam.nextX, beam.nextY, beam.nextX, beam.nextY + 1)
                    toAppend.append(newBeam)
                    print(beam.x, beam.y)
                    print(beam.nextX, beam.nextY)
                    print(newBeam.x, newBeam.y)
                    print(newBeam)
            elif inputArray[beam.nextY][beam.nextX] == "-":
                if beam.nextX == beam.x+1:
                    beam.itarate(beam.nextX+1, beam.nextY)
                elif beam.nextX == beam.x-1:
                    beam.itarate(beam.nextX-1, beam.nextY)
                else:
                    beam.itarate(beam.nextX-1, beam.nextY )
                    newBeam = Beam(beam.nextX, beam.nextY, beam.nextX+1, beam.nextY)
                    toAppend.append(newBeam)

    for newBeam in toAppend:
        allBeams.append(newBeam)
    for beams in allBeams:
        if beams.x < 0 or beams.x > len(inputArray[0]) or beams.y < 0 or beams.y > len(inputArray):
            allBeams.remove(beams)
    for beams in allBeams:
        currentcoords = [beam.x, beam.y]
        if currentcoords not in touchedCoords:
            touchedCoords.append(currentcoords)

print(inputArray)
print(len(touchedCoords))
print(touchedCoords)
