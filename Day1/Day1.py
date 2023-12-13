with open('input.txt') as my_file:
    testsite_array = my_file.readlines()

sol = []
temp = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def isNr(testStr, index):
    if(testStr[index]=="o" and testStr[index+1]=="n" and testStr[index+2]=="e"):
        return 1
    elif(testStr[index]=="t" and testStr[index+1]=="w" and testStr[index+2]=="o"):
        return 2
    elif (testStr[index] == "t" and testStr[index + 1] == "h" and testStr[index + 2] == "r"and testStr[index + 3] == "e"and testStr[index + 4] == "e"):
        return 3
    elif (testStr[index] == "f" and testStr[index + 1] == "o" and testStr[index + 2] == "u" and testStr[index + 3] == "r"):
        return 4
    elif (testStr[index] == "f" and testStr[index + 1] == "i" and testStr[index + 2] == "v" and testStr[index + 3] == "e"):
        return 5
    elif (testStr[index] == "s" and testStr[index + 1] == "i" and testStr[index + 2] == "x"):
        return 6
    elif (testStr[index] == "s" and testStr[index + 1] == "e" and testStr[index + 2] == "v"and testStr[index + 3] == "e"and testStr[index + 4] == "n"):
        return 7
    elif (testStr[index] == "e" and testStr[index + 1] == "i" and testStr[index + 2] == "g"and testStr[index + 3] == "h"and testStr[index + 4] == "t"):
        return 8
    elif (testStr[index] == "n" and testStr[index + 1] == "i" and testStr[index + 2] == "n" and testStr[index + 3] == "e"):
        return 9
    else:
        return 0


for i in range (0,len(testsite_array)):
    first = -1
    last = -1

    for j in range(0, len(testsite_array[i])):
        char = testsite_array[i][j]
        try:
            integer = int(char)
            if(first == -1):
                first = integer
            else:
                last=integer
        except:
            temp = isNr(testsite_array[i],j)
            if(temp != 0):
                if(first == -1):
                    first = temp
                else:
                    last = temp
    if(last == -1):
        combined = str(str(first)+str(first))
    else:
        combined = str(str(first)+str(last))
    sol.append(combined)

final = 0
for el in sol:
    final += int(el)

print(final)