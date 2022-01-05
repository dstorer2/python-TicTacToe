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
        self.play()
    
    def play(self):
        while not self.game_over:
            move = receivePlayerInput()
            if not validateInput(move, self.board.size):
                return self.play()
            if not self.board.checkIsEmpty(move):
                return self.play()
            self.board.updateBoard(move, self.XTurn)
            self.board.displayBoard()
            if self.board.checkForVictory(self.XTurn, self.winningCombos) or self.board.checkForCatsGame():
                self.game_over = True
                return
            self.switchTurns()

    def switchTurns(self):
        self.XTurn = not self.XTurn


new_game = Game()
new_game.startGame()