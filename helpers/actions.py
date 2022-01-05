def makeAMove(size, XTurn):
    maxIndex = size**2
    player = "X"
    if not XTurn:
        player = "O"
    print("%s's turn!" %player)
    move = receivePlayerInput()
    if not validateInput(receivePlayerInput(), maxIndex):
        print("Please enter a valid integer between 1 and %s" %maxIndex)
        return makeAMove()
    return move

def receivePlayerInput():
    move = input("Please enter the number of the space in which you wish to play\n")
    print("You chose %s" %move)
    return move

def validateInput(move, size):
    maxIndex = size**2
    isValid = True
    print("Validating input")
    try:
        num = int(move)
    except:
        print("Invalid input: Please enter a number")
        isValid = False
        return isValid
    if num < 1 or num > maxIndex:
        print("Invalid input: Please enter an integer from the board")
        isValid = False
    return isValid

def getWinningCombos(size):
    winningCombos = []
    i = 0
    diag1 = []
    diag2 = []
    while i < size:
        horiz = []
        vert = []
        diag1.append(1 + i * (1 + size))
        diag2.append(size + i * (size-1))
        j = 1
        while j <= size:
            horiz.append((i*size)+j)
            vert.append((i+1) + (j-1)*size)
            j +=1
        i +=1
        winningCombos.append(horiz)
        winningCombos.append(vert)
    winningCombos.append(diag1)
    winningCombos.append(diag2)
    return winningCombos

