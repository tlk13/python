import time

def evaluate(list):

    z = zeroes(list)
    (solution,sol) = backtrack(list,z, len(z), 0)
    return solution

#backtrack algorithm
def backtrack(list, zers, zerslen, n):
    if n == zerslen:  return (list, 2)
    (x,y) = zers[n]
    nlist = list

    for z in range(1,10):
        nlist[y][x] = z
        if valid (nlist, (x,y), z):
            (nnlist, sol) = backtrack(nlist, zers, zerslen, n+1)
            if(sol) == 2:
                return (nnlist,2)
        nlist[y][x] = 0
    return (list, 0)

#findsAllZeroes
def zeroes(list):
    zers = []
    for x in range(9):
        for y in range(9):
            if list[y][x] ==0:
                zers.append((x,y))
    return zers


#check if combination is valid:
def valid(list, tupl, change):
    (x,y) = tupl

    if change in (list[y][:(x)]+list[y][(x+1):]):
        return False

    lina = [i[x] for i in list]
    if change in (lina[:y]+lina[(y+1):]):
        return False

    bx = x // 3
    by = y // 3
    pos = x%3+3*(y%3)
    line = []
    for s in range(3):
        for t in range(3):
            line.append(list[s+3*by][t+3*bx])
    if change in (line[:pos]+line[(pos+1):]):
        return False
    return True




t = [[9,6,0,0,5,4,0,2,8],[0,0,0,9,0,2,5,0,0],[0,0,4,8,0,0,0,1,0],
    [0,0,0,6,4,3,0,0,0],[0,0,6,0,0,0,2,0,0],[0,0,0,1,2,8,0,0,0],
    [0,4,0,0,0,5,1,0,0],[0,0,9,4,0,7,0,0,0],[7,5,0,2,6,0,0,4,9]]

startTime = time.time()
for x in evaluate(t): print(x)
endTime = time.time()
print("Time elapsed: " + str(endTime-startTime) +"sec")




ttt=[[9, 6, 0, 0, 5, 4, 0, 2, 8],
[0, 0, 0, 9, 0, 2, 5, 0, 0],
[0, 0, 4, 8, 0, 0, 0, 1, 0],
[0, 0, 0, 6, 4, 3, 0, 0, 0],
[0, 0, 6, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 1, 2, 8, 0, 0, 0],
[0, 4, 0, 0, 0, 5, 1, 0, 0],
[0, 0, 9, 4, 0, 7, 0, 0, 0],
[7, 5, 0, 2, 6, 0, 0, 4, 9]]


diff= [[9, 6, 0, 0, 5, 4, 0, 2, 8],
[0, 0, 0, 9, 0, 2, 5, 0, 0],
[0, 0, 4, 8, 0, 0, 0, 1, 0],
[0, 0, 0, 6, 4, 3, 0, 0, 0],
[0, 0, 6, 0, 0, 0, 2, 0, 0],
[0, 0, 0, 1, 2, 8, 0, 0, 0],
[0, 4, 0, 0, 0, 5, 1, 0, 0],
[0, 0, 9, 4, 0, 7, 0, 0, 0],
[7, 5, 0, 2, 6, 0, 0, 4, 9]]
