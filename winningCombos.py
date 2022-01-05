def checkForVictory(size):
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
    

checkForVictory(4)