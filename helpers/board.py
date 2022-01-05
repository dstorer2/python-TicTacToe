from cell import *

class Board:
    def __init__(self, size = 3):
        self.grid = []
        self.size = size
    
    def populateBoard(self):
        i=0
        spaceindex = 1
        while i < self.size:
            j=0
            while j < self.size:
                self.grid.append(Cell(spaceindex))
                j +=1
                spaceindex +=1
            i +=1
    
    def displayBoard(self):
        print(" ")
        horizontalBreak = "-"*((self.size*4)-1)
        verticalSpace = " | "
        i=0
        j=0
        lineBreak = self.size
        while i < self.size:
            row = " "
            while j < lineBreak:
                cell = self.grid[j]
                displayAttribute = cell.value
                if not displayAttribute:
                    displayAttribute = cell.index
                row +=str(displayAttribute)
                if j != lineBreak-1:
                    row +=verticalSpace
                j +=1
            if i != self.size-1:
                print(row)
                print(horizontalBreak)
            else:
                print(row)
            i +=1
            lineBreak += self.size
        print(" ")
    
    def checkIsEmpty(self, move):
        isEmpty = True
        if self.grid[int(move)-1].value:
            isEmpty = False
            print("That space has already been taken. Please select another space")
        return isEmpty

    def updateBoard(self, move, player):
        value = "O"
        if player:
            value = "X"
        self.grid[int(move)-1].value = value
    
    def checkForVictory(self, playerX, winningCombos):
        winner = False
        playerValue = "O"
        if playerX:
            playerValue = "X"
        for combo in winningCombos:
            allMatch = True
            for num in combo:
                if self.grid[num-1].value != playerValue:
                    allMatch =False
            if allMatch:
                winner = True
            if winner:
                print("%s wins!" %playerValue)
                return winner
        return winner
    
    def checkForCatsGame(self):
        catsGame = True
        for cell in self.grid:
            if not cell.value:
                catsGame = False
        if catsGame:
            print("It's a cats game!")
        return catsGame

