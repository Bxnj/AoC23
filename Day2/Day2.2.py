with open('florianday2') as my_file:
    inputArray = my_file.readlines()
print(inputArray)
sol = 0

for i in range(0, len(inputArray)):
    ##print(inputArray[i])
    id = int(inputArray[i].split(":")[0].split(" ")[1])
    ##print(id)
    pulls = inputArray[i].split(":")[1].split(";")
    print(pulls)
    redMax = 0
    blueMax = 0
    greenMax = 0
    for j in range(0 , len(pulls)):
        seperated = pulls[j].split(",")
        for k in range(0, len(seperated)):
            number = int(seperated[k].split(" ")[1])
            color = seperated[k].split(" ")[2].replace("\n", "")
            if(color == "red"):
                if(number > redMax):
                    redMax = number
            elif(color == "blue"):
                if (number > blueMax):
                    blueMax = number
            elif(color == "green"):
                if (number > greenMax):
                    greenMax = number
            else:
                print("SHIT")
    sol += redMax*blueMax*greenMax


print(sol)