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



def recFind(y, max,inputArray):
    final = 0
    for x in range(y, max):
        if dp[x] != -1:
            final += dp[x]
        else:
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
            nrWinners = getNrWinners(winning, have)
            if nrWinners > 0:
                temp = recFind(x,x+nrWinners,inputArray)
            else:
                temp = 0
            recNr = nrWinners+temp
            dp[x] = recNr
            final+=recNr
    return final


final = recFind(0, len(inputArray),inputArray)





print( final)