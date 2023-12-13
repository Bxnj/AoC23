import util as ut

strenght=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

def sortByStrenght(toSort, strength, starterString):
    ret = []
    for l in range(0, len(strength)):
        k = [item for item in toSort if item[0].startswith(starterString + strength[l])]
        if len(k) == 1:
            ret.append(k[0])
        elif len(k) != 0:
            new = sortByStrenght(k, strength, starterString+strength[l])
            for d in range(0,len(new)):
                ret.append(new[d])
    return ret

with open('input.txt') as my_file:
    inputArray = my_file.readlines()

for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")

sol=[]
parsedList = []
for i in range(0, len(inputArray)):
    winnings = int(inputArray[i].split(" ")[1])
    hand = inputArray[i].split(" ")[0]
    combinedParsed = [hand, winnings]
    #print(combinedParsed)
    parsedList.append(combinedParsed)

print(parsedList)
print(sortByStrenght(parsedList,strenght, ""))
#5 of a kind
temp = []
five = []
todel = []
for h in range(0, len(parsedList)):
    if parsedList[h][0][0]==parsedList[h][0][1] and parsedList[h][0][0]==parsedList[h][0][2]and parsedList[h][0][0]==parsedList[h][0][3] and parsedList[h][0][0]==parsedList[h][0][4]:
        tem = parsedList[h]
        todel.append(tem)
        tem.append(parsedList[h][0][0])
        five.append(tem)
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
for l in range(0, len(strenght)):
    for e in range(0, len(five)):
        if(five[e][2]==strenght[l]):
            sol.append([five[e][0], five[e][1]])
#print(five)

#four of a kind
todel = []
four = []
for q in range(0, len(parsedList)):
    if parsedList[q][0].count(parsedList[q][0][0]) == 4 or parsedList[q][0].count(parsedList[q][0][1]) == 4:
        todel.append(parsedList[q])
        four.append(parsedList[q])
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
#print(four)
sortedFour = sortByStrenght(four,strenght,"")
for z in range(0 ,len(sortedFour)):
    sol.append(sortedFour[z])


#full house
full = []
todel = []
for z in range(0, len(parsedList)):
    if len(set(parsedList[z][0])) == 2:
        full.append(parsedList[z])
        todel.append(parsedList[z])
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
sortedFull = sortByStrenght(full,strenght,"")
for z in range(0 ,len(sortedFull)):
    sol.append(sortedFull[z])

#3 of a kind
todel = []
three = []
for q in range(0, len(parsedList)):
    if parsedList[q][0].count(parsedList[q][0][0]) == 3 or parsedList[q][0].count(parsedList[q][0][1]) == 3 or parsedList[q][0].count(parsedList[q][0][2]) == 3:
        three.append(parsedList[q])
        todel.append(parsedList[q])
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
sortedThree = sortByStrenght(three,strenght,"")
for z in range(0 ,len(sortedThree)):
    sol.append(sortedThree[z])




#two pairs
todel = []
twopairs = []
for q in range(0, len(parsedList)):
    if len(set(parsedList[q][0])) == 3:
        twopairs.append(parsedList[q])
        todel.append(parsedList[q])
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
sortedTwoPairs = sortByStrenght(twopairs,strenght,"")
for z in range(0 ,len(sortedTwoPairs)):
    sol.append(sortedTwoPairs[z])

#one pairs
todel = []
pair = []
for q in range(0, len(parsedList)):
    if len(set(parsedList[q][0])) == 4:
        pair.append(parsedList[q])
        todel.append(parsedList[q])
for e in range(0,len(todel)):
    parsedList.remove(todel[e])
sortedPairs = sortByStrenght(pair,strenght,"")
for z in range(0 ,len(sortedPairs)):
    sol.append(sortedPairs[z])

sortedRest = sortByStrenght(parsedList,strenght,"")
for i in range(0, len(sortedRest)):
    sol.append(sortedRest[i])

sol.reverse()
print(sol)
final = 0

for l in range(0, len(sol)):
    final = final+ (sol[l][1]*(l+1))
print(final)