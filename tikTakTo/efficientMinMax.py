##################################################################################
## Actual AI code that deals with the MinMax problem posed by TikTakToo ##
##################################################################################

# Identifies the Maximum Value achievable for the computer player (best move)
def maxValue(field, fieldsMarked, position, playerOne):
    value = -100
    for y in range(3):
        for x in range(3):
            if field[y][x]==" . ":
                field[y][x]= " O "
                value = max(value, valueOfState(field, fieldsMarked+1, (y,x),  playerOne))
                field[y][x]= " . "
                if value > 0: return value
    return value

# Identifies the Minimum value
# worst case scenario for the computer, i.e. best outcome for human player
def minValue(field, fieldsMarked, position, playerOne):
    value = 100
    for y in range(3):
        for x in range(3):
            if field[y][x]==" . ":
                field[y][x]= " X "
                value = min(value, valueOfState(field, fieldsMarked+1, (y,x),  playerOne))
                field[y][x]= " . "
                if value < 0: return value
    return value

# evaluates the value of state of the game for the computer player
# if the state is terminal (i.e. someone won or it is a draw), it returns the
# utilities -10, 0, 10 for each outcome scenario
# else it goes into the next round of possible states with the minMax approach
# which try to evaluate it
def valueOfState(field, fieldsMarked, position, playerOne):
    if fieldsMarked > 4:
        if playerOne:
            if checkWinner(field, fieldsMarked, position, playerOne): return -10
        else:
            if checkWinner(field, fieldsMarked, position, playerOne): return 10
        if fieldsMarked == 9:                                         return 0
    playerOne = not playerOne
    if playerOne:   return minValue(field, fieldsMarked, position, playerOne)
    return maxValue(field, fieldsMarked, position, playerOne)

# cycles through the possible moves for the computer player and returns
# the play with the highest utility
def nextMove(field, fieldsMarked, playerOne):
    moves = []; values = []
    for y in range(3):
        for x in range(3):
            if field[y][x] == " . ":
                field[y][x] = " O "
                moves.append((y,x)); values.append(valueOfState(field, fieldsMarked+1, (y,x), False))
                field[y][x] = " . "
    if 10 in values: return moves[values.index(10)]
    if 0 in values:  return moves[values.index(0)]
    return moves[values.index(-10)]

# plays the move with the highest utility
def makeMove(field, fieldsMarked, playerOne):
    y,x = nextMove(field, fieldsMarked, playerOne)
    field[y][x] = " O "
    return (y,x)

##################################################################################
## GUI and game dynamics that allows us to corretly play TikTakToo ##
##################################################################################

# checks if the user corretly inputs the coordinates, does not work for non-integers
def getUserInput():
    xCooVal, yCooVal = (False, False)
    while not xCooVal:
        xCoo = int(input("Please enter x coordinate!\n"))
        if xCoo > 0 and xCoo < 4: xCooVal=True
        else: print("Input was incorrect, please try again!")
    while not yCooVal:
        yCoo = int(input("Please enter y coordinate!\n"))
        if yCoo > 0 and yCoo < 4: yCooVal=True
        else: print("Input was incorrect, please try again!")
    return (yCoo, xCoo)

# enters the right coordinates from the user in the field and returns these
# as a tuple
def registerUserInput(field, playerOne):
    valid = False
    while not valid:
        y, x = getUserInput()
        if field[-(y%3)][x-1] != " . ":
            print("Please try again, this field has already been marked by a player!")
        else: valid = True
    if playerOne: field[-(y%3)][x-1] = " X "
    else: field[-(y%3)][x-1] = " O "
    return (-(y%3), x-1)

# prints the playing field to the console
def printField(field):
    for y in range(3):
        for x in range(3):
            print(field[y][x], end="")
        print()

# checks if a move made by the players is valid or not
def checkValid(field, position):
    y, x = position
    return field[y][x] == " . "

# simply checks if the latest move (position) resulted in a win for the
# player who is currently playing (playerOne is a boolean)
# works faster as in case the amount of fieldsMarked is low, then there cannot be a winner
def checkWinner(field, fieldsMarked, position, playerOne):
    if fieldsMarked < 5:
        return False
    playerSign = ""
    y,x = position
    if playerOne: playerSign = " X "
    else: playerSign = " O "
    if field[0][x] == field[1][x] == field[2][x] == playerSign: return True
    if field[y][0] == field[y][1] == field[y][2] == playerSign: return True
    if (y+y)%2==0:
        if field[0][0]==field[1][1]==field[2][2]==playerSign or \
            field[2][0]==field[1][1]==field[0][2]==playerSign:
            return True
    return False


##################################################################################
## Here the game is commenced plus the main loop is started ##
##################################################################################

# initializes / resets the playing field and gives helpful info
def introduce():
    field = [[" . " for x in range(3)] for x in range(3)]
    print("\n\n"+80*"-"+"\nWelcome to the game of TikTakToo, you have the first move.\n" +
    "Beware, the computer know of any weaknesses in your strategy.")
    printField(field)
    return (field, 0, True)

# creates the important variables
field = [[]]; fieldsMarked = 0; playerOne = True
field, fieldsMarked, playerOne = introduce()

while True:
    if fieldsMarked == 9:
        print("The Game has ended, do you want to play another round? \n Type 'y' for yes and 'n' for no.")
        s = input()
        if s == "y":
            introduce(); continue
        elif s == "n":   print("Thank you for playing! Come back anytime!"); break
        else:            print("You did not answer correctly, please look out again!"); continue

    if playerOne: print("Your turn: ");move = registerUserInput(field, playerOne)
    else:         move = makeMove(field, fieldsMarked, playerOne); print("The computer played: ")

    fieldsMarked += 1
    printField(field)
    if checkWinner(field, fieldsMarked, move, playerOne):
         print("Player " + str((not playerOne) + 1) + " has won!"); fieldsMarked = 9; continue


    playerOne = not playerOne







#test
