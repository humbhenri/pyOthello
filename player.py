#!/usr/bin/env python
""" player.py Humberto Henrique Campos Pinheiro 
Human and Computer classes
"""

from evaluator import Evaluator
from config import WHITE, BLACK
from minimax import Minimax
import random


def change_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK


class Human:

    """ Human player """

    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui

    def get_move(self):
        """ Uses gui to handle mouse
        """
        validMoves = self.current_board.get_valid_moves(self.color)
        while True:
            move = self.gui.get_mouse_input()
            if move in validMoves:
                break
        self.current_board.apply_move(move, self.color)
        return 0, self.current_board

    def get_current_board(self, board):
        self.current_board = board


class Computer(object):

    def __init__(self, color, prune=3):
        self.depthLimit = prune
        evaluator = Evaluator()
        self.minimaxObj = Minimax(evaluator.score)
        self.color = color

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        return self.minimaxObj.minimax(self.current_board, None, self.depthLimit, self.color,
                                       change_color(self.color))


class RandomPlayer (Computer):

    def get_move(self):
        x = random.sample(self.current_board.get_valid_moves(self.color), 1)
        return x[0]
