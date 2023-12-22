def isSymbolAroundFull(x,y,Array,symbol):
    result = isSymbolAroundDirect(x,y,Array,symbol)
    if len(Array[x]) < y and len(Array) < x:
        if Array[x+1][y+1] == symbol:
            result = True

    if len(Array[x]) < y and x > 0:
        if Array[x-1][y+1] == symbol:
            result = True

    if y > 0 and len(Array) < x:
        if Array[x+1][y-1] == symbol:
            result = True

    if y > 0 and x > 0:
        if Array[x-1][y-1] == symbol:
            result = True
    return result


def isSymbolAroundDirect(x,y,Array,symbol):
    result = False
    if len(Array[x]) < y:
        if Array[x][y+1] == symbol:
            result = True
    if y > 0:
        if Array[x][y - 1] == symbol:
            result = True
    if len(Array) < x:
        if Array[x+1][y] == symbol:
            result = True
    if x > 0:
        if Array[x-1][y] == symbol:
            result = True
    return result