from helpers.board import *
from helpers.actions import *
import math

class Game:
    def __init__(self, game_over = False, XTurn = True, boardSize = 3):
        self.game_over = game_over
        self.XTurn = XTurn
        self.board = Board(boardSize)
        self.winningCombos = getWinningCombos(boardSize)

    def startGame(self):
        self.board.populateBoard()
        self.board.displayBoard()
        while not self.game_over:
            self.play()
    
    def play(self):
        move = receivePlayerInput()
        if not self.validations(move):
            return
        self.board.updateBoard(move, self.XTurn)
        self.board.displayBoard()
        if self.board.checkForVictory(self.XTurn, self.winningCombos) or self.board.checkForCatsGame():
            self.game_over = True
        self.XTurn = not self.XTurn
    
    def validations(self, move):
        isValid = False
        if validateInput(move, self.board.size):
            if self.board.checkIsEmpty(move):
                isValid = True
        return isValid

new_game = Game()
new_game.startGame()