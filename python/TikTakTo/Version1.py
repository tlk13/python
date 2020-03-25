import copy

def printPlayingField(fi):
    counter = 0
    for x in fi:
        for y in fi[counter]:
            print y,
        print ""
        counter +=1
    print "\n"

def getUserInput():
    xCooVal = False
    yCooVal = False
    while not xCooVal:
        xCoo = input("Please enter x coordinate!\n")
        if xCoo > 0 and xCoo < 4: xCooVal=True
        else: print "Input was incorrect, please try again!"
    while not yCooVal:
        yCoo = input("Please enter y coordinate!\n")
        if yCoo > 0 and yCoo < 4: yCooVal=True
        else: print "Input was incorrect, please try again!"
    coordinates = [xCoo, yCoo]
    return coordinates

def registerUserInput():
    valid = False
    coordinates = []
    while not valid:
        coordinates = getUserInput()
        if field[abs(coordinates[1]-3)][abs(coordinates[0]-1)] == "X" or field[abs(coordinates[1]-3)][abs(coordinates[0]-1)] == "O": print "Please try again, this field has already been marked by you!"
        else: valid = True
    field[abs(coordinates[1]-3)][abs(coordinates[0]-1)] = "X"
    print "User Input recognized, here is the updated playing Field:\n"

def checkIfWinner(fie):
    winnerList = [False]

    #check horizontal check Winner
    for x in fie:
        if x[0] == "X" and x[1] == "X" and x[2] == "X":
            winnerList[0]=True; winnerList.append(1)
            return winnerList
        if x[0] == "O" and x[1] == "O" and x[2] == "O":
            winnerList[0]=True; winnerList.append(2)
            return winnerList

    #check vertical check Winner
    for i in range(3):
        if fie[0][i] == "X" and  fie[1][i] == "X" and  fie[2][i] == "X":
            winnerList[0]=True; winnerList.append(1)
            return winnerList
        if fie[0][i] == "O" and  fie[1][i] == "O" and  fie[2][i] == "O":
            winnerList[0]=True; winnerList.append(2)
            return winnerList

    #check diagonal check Winner
    if (fie[0][0] == "X" and fie[1][1] == "X" and fie[2][2] == "X") or (fie[0][2] == "X" and fie[1][1] == "X" and fie[2][0] == "X"):
        winnerList[0]=True; winnerList.append(1)
        return winnerList
    if (fie[0][0] == "O" and fie[1][1] == "O" and fie[2][2] == "O") or (fie[0][2] == "O" and fie[1][1] == "O" and fie[2][0] == "O"):
        winnerList[0]=True; winnerList.append(2)
        return winnerList
    else: return winnerList

def checkIfTerminal(fie):
    if checkIfWinner(fie)[0]:
        return True
    elif checkIfFull(fie):
        return True
    else:
        return False

def checkIfFull(fie):
    counter = 0
    for x in fie:
        for i in range(3):
            if not x[i] == ".": counter+=1
    if counter == 9: return True
    else: return False

def checkUtility(fie):
    if checkIfFull(fie) == True and checkIfWinner(fie)[0] == False:
        return 0
    if checkIfWinner(fie)[0]:
        if checkIfWinner(fie)[1] == 1:
            return (-10)
        else:
            return 10
    pass

def introduction():
    print "Welcome to this game of TikTakTo"
    print "You will proceed by entering the coordinates where you would like to make your X, by typing the x coordinate and then the y coordinate"

    print "Here is you playing field: "

    printPlayingField(field)

def valueOfState(fie, ma):
    if checkIfTerminal(fie):
        return checkUtility(fie)
    elif ma:
        return maxValue(fie)
    else:
        return minValue(fie)

def maxValue(fie):
    v = -1000
    for x in range(3):
        for y in range(3):
            if fie[x][y] == ".":
                fi = copy.deepcopy(fie)
                fi[x][y]="O"
                v = max(v, valueOfState(fi, False))
    return v

def minValue(fie):
    v = 1000
    for x in range(3):
        for y in range(3):
            if fie[x][y] == ".":
                fi = copy.deepcopy(fie)
                fi[x][y]="X"
                v = min(v, valueOfState(fi, True))
    return v


def playNextMove():
    print "Checking next move"
    moveFound = False
    xCC, yCC = 0,0
    for x in range(3):
        for y in range(3):
            if field[x][y] == ".":
                fi = copy.deepcopy(field)
                fi[x][y]="O"
                if valueOfState(fi, False) > 0:
                    moveFound = True
                    xCC, yCC = x,y
    if not moveFound:
        print "Checking Neutral Options"
        for x in range(3):
            for y in range(3):
                if field[x][y] == ".":
                    fi = copy.deepcopy(field)
                    fi[x][y]="O"
                    if valueOfState(fi, False) == 0:
                        moveFound = True
                        xCC, yCC = x,y
    if not moveFound:
        print "checkign negative optioms"
        for x in range(3):
            for y in range(3):
                if field[x][y] == ".":
                    fi = copy.deepcopy(field)
                    fi[x][y]="O"
                    if valueOfState(fi, False) < 0:
                        moveFound = True
                        xCC, yCC = x,y
    field[xCC][yCC] = "O"

#setUp
field = [["." for y in range(3)] for x in range(3)]
gameWon = False
wantToPlay = True
introduction()

#mainLoop
while wantToPlay:
    while not gameWon:
        registerUserInput()
        printPlayingField(field)
        gameWon = checkIfWinner(field)[0]
        if gameWon:
            print "Player ", checkIfWinner(field)[1], " won the game, Congratulations!!"; break
        if checkIfFull(field):
            print "The game terminated, the field is too full :("; break
        playNextMove()
        printPlayingField(field)
        gameWon = checkIfWinner(field)[0]
        if gameWon:
            print "Player ", checkIfWinner(field)[1], " won the game, You were beaten by a Computer!!"; break
        if checkIfFull(field):
            print "The game terminated, the field is too full :("; break
    inputValid = False
    while not inputValid:
        s = raw_input("Do you want to continue? - answer with 'y' or 'n'\n")
        if s == "n":
            print "The game terminated"
            wantToPlay = False
            inputValid = True
            break
        elif s == "y":
            print "Another round! \n"
            inputValid = True
            gameWon = False
            field = [["." for y in range(3)] for x in range(3)]
            printPlayingField(field)
            break
        else:
            print "This is not valid input, please repeat"
            inputValid = False
