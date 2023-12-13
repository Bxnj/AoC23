import sys
sys.setrecursionlimit(1500)
with open('input.txt') as my_file:
    inputArray = my_file.readlines()
print(inputArray)

dp = []
for k in range(0, len(inputArray)):
    inputArray[k] = inputArray[k].replace("\n", "")
    dp.append(-1)
print(inputArray)
print(dp)
def getNrWinners(winners, have):
    nrWinners = 0
    for e in range(0, len(have)):
        if have[e] in winners:
            nrWinners += 1
    return  nrWinners

def WinnerNr(inputArray):
    winnerArray=[]
    for x in range(0, len(inputArray)):
        relevant = inputArray[x].split(":")[1]
        winning = relevant.split("|")[0].split(" ")
        have = relevant.split("|")[1].split(" ")
        for k in range(0, len(winning)):
            if winning[k] != "":
                winning[k] = int(winning[k])
        while True:
            if "" in winning:
                winning.remove("")
            else:
                break
        for k in range(0, len(have)):
            if have[k] != "":
                have[k] = int(have[k])
        while True:
            if "" in have:
                have.remove("")
            else:
                break
        winnerArray.append(getNrWinners(winning, have))
    return winnerArray


winArr = WinnerNr(inputArray)
print(winArr)
def recFind(x, winArr):
    if winArr[x] == 0:
        dp[x] = 1
    if dp[x] != -1:
        return dp[x]
    else:
        ad = 0
        for i in range(x+1, x+winArr[x]+1):
            ad+=recFind(i,winArr)
        dp[x] = ad+1
        return ad+1



for l in range(0, len(winArr)):
    recFind(l, winArr)
finals = 0
print(dp)
for i in range(0,len(dp)):
    finals+= dp[i]



print( finals)