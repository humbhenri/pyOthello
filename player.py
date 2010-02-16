#!/usr/bin/env python
""" player.py Humberto Henrique Campos Pinheiro 
Human and Computer classes
"""

import ui
import board
from copy import deepcopy
import random

INFINITY = 999999999
MAX = 0
MIN = 1
BLACK = 1
WHITE = 2

def id ( color ):
    if color == BLACK:
        return 'black'
    else:
        return 'white'

def change_color ( color ):
    if color == BLACK:
        return WHITE
    else:
        return BLACK


class Evaluator(object):	
	WIPEOUT_SCORE = 1000 	#a move that results a player losing all pieces
	PIECE_COUNT_WEIGHT = [0, 0, 0, 4, 1]
	POTENTIAL_MOBILITY_WEIGHT= [5, 4, 3, 2, 0]
	MOBILITY_WEIGHT = [7, 6, 5, 4, 0]
	CORNER_WEIGHT= [35, 35, 35, 35, 0]
	EDGE_WEIGHT = [0, 3, 4, 5, 0]
	XSQUARE_WEIGHT = [-8, -8, -8, -8, 0]
	
	def __init__( self, player ):		
		self.player = player
		self.enemy = change_color( player )
		
	def score( self, startBoard, board, currentDepth, searchDepth ):
		""" Determine the score of the given board for the specified player.
		- startBoard the board before any move is made
		- board the board to score
		- currentDepth depth of this leaf in the game tree
		- searchDepth depth used for searches. 
		"""
		sc = 0
		blacks, whites = board.count_stones()
		deltaBoard = board.compare( startBoard )		
		deltaCount = deltaBoard.get_count()
		
		# check wipe out
		if (self.player == WHITE and whites = 0) or (self.player == BLACK and blacks = 0):
			return sc = -WIPEOUT_SCORE
			
		# determine weigths according to the number of pieces
		piece_count = board.get_count()
		band = 0
		if piece_count <= 16: 
			band = 0
		elif piece_count <= 32: 
			band = 1
		elif piece_count <= 48: 
			band = 2
		elif piece_count <= 64 - currentDepth:
			band = 3
		elif:
			band = 4
		
		if PIECE_COUNT_WEIGHT[band] != 0:
			# piece differential
			myScore = deltaBoard.get_count(self.player)
			yourScore = deltaBoard.get_count(self.enemy)
			sc = sc + PIECE_COUNT_WEIGHT[band] * ( myScore - yourScore )
		
		if CORNER_WEIGHT[band] != 0:
			# corner differential
			myScore = 0
			yourScore = 0
			for i in [0, 7]:
				for j in [0, 7]:
					if board.board[i][j] == self.player:
						myScore += 1
					else:
						yourScore += 1
					if myScore + yourScore >= deltaCount:
						break
				if myScore + yourScore >= deltaCount:
					break
			sc += CORNER_WEIGHT[band] * ( myScore - yourScore )
		
		return sc
		

# this is bad
def evaluate ( board, who ):
    """ Evaluate board, returns a score    
    """
    bl_pie, wh_pie = board.count_stones()
    if bl_pie + wh_pie > 60:
	# Game is ending, prioritizes pieces difference
        if who == WHITE:
            if wh_pie == 0:
                return -INFINITY
            elif bl_pie == 0:
                return INFINITY
        else:
            if wh_pie == 0:
                return INFINITY
            elif bl_pie == 0:
                return -INFINITY
        if who == WHITE:
            return wh_pie - bl_pie
        else:
            return bl_pie - wh_pie
             
            
    mob_wght = 0.75
    weights = [[ 30, -2 , 0, 0, 0, 0, -2, 30], \
	        	[-2 ,-5, 0, 0, 0, 0,-5, -2],\
	        	[0 , 0, 0, 0, 0, 0, 0, 0],\
		        [0 , 0, 0, 0, 0, 0, 0, 0],\
		        [0 , 0, 0, 0, 0, 0, 0, 0],\
		        [0 , 0, 0, 0, 0, 0, 0, 0],\
		        [-2 ,-5, 0, 0, 0, 0,-5, -2],\
		        [30, -2, 0, 0, 0, 0,-2 , 30]]

    # game end score
    if bl_pie + wh_pie > 55:
        mob_wght = 0
        weights = [[ 15, 2 , 2, 2, 2, 2, 2, 15], \
            [2 ,-2, 0, 0, 0, 0,-2, 2],\
            [2 , 0, 0, 0, 0, 0, 0, 2],\
            [2 , 0, 0, 0, 0, 0, 0, 2],\
            [2 , 0, 0, 0, 0, 0, 0, 2],\
            [2 , 0, 0, 0, 0, 0, 0, 2],\
            [2 ,-2, 0, 0, 0, 0,-2, 2],\
            [15, 2, 2, 2, 2, 2, 2 , 15]]

    # static evaluation
    temp = board.board
    score = 0
    enemy = change_color ( who )
    for i in range ( 8 ):
        for j in range ( 8 ):
            if temp[i][j] == who:
                score += weights[i][j]
            elif temp[i][j] == enemy:
                score += weights[i][j]
    
    if who == WHITE:
        score += wh_pie - bl_pie
    else:
        score += bl_pie - wh_pie 
    
    # tries to lower opponent mobility
    my_no_moves = len ( board.get_valid_moves ( who ) )
    en_no_moves = len ( board.get_valid_moves ( enemy ) )
    score += mob_wght * ( my_no_moves - en_no_moves )

    return score
    

class Human:
    """ Human player """

    def __init__( self, gui, color="black" ):
        self.color = color
        self.gui = gui

    def get_move ( self ):
        """ Uses gui to handle mouse
        """
        return self.gui.get_mouse_input()

    def get_current_board ( self, board ):
        """ Only included to maintain the same interface of Computer class
        """
        pass
    

class Computer:
    """ Represents computer player. Uses Minimax with Alpha-Beta pruning
    """
    
    def __init__ ( self, color, cutoff=3 ):
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.color = color
        if color == self.BLACK:
            self.enemy_color = self.WHITE
        else:
            self.enemy_color = self.BLACK        
        self.current_board = None
        self.depth_limit = cutoff
        self.MAX = 1
        self.MIN = 0
        
    
    def change_color ( self, color ):
        if color == self.BLACK:
            return self.WHITE
        else:
            return self.BLACK
    
    def get_current_board ( self, board ):
        """ Current board state. """
        self.current_board = board


    def get_move ( self ):
        """ Best move according to minimax algorithm and board 
	    state evaluation function evaluate
        """        
        return self.__max_value ( self.color, self.current_board, \
                    -INFINITY, INFINITY, self.depth_limit, True )

    def __max_value ( self, color, state, alpha, beta, depth, return_action=False ):
        if state.game_ended() or depth == 0:
            return self.eval ( state, color )

        moves = state.get_valid_moves ( color )
        e_color = change_color ( color )
        best_move = None
        val = -INFINITY
        if moves == []:
            return self.__min_value ( e_color, state, alpha, beta, depth-1 )

        for move in moves:
            new_st = deepcopy ( state )
            new_st.apply_move ( move, color )
            v = self.__min_value ( e_color, new_st, alpha, beta, depth-1 )
            if v > val:
                val = v
                best_move = move
            if v >= beta:
                if return_action == True:
                    return best_move
                else:
                    return beta
            alpha = max ( val, alpha )

        if return_action == True:
            return best_move
        else:
            return v

    def __min_value ( self, color, state, alpha, beta, depth ):
        if state.game_ended() or depth == 0:
            return self.eval ( state, color )

        e_color = change_color ( color )                    
        moves = state.get_valid_moves ( color )
        if moves == []:
            return self.__max_value ( e_color, state, alpha, beta, depth-1 )
            
        v = INFINITY
        for move in moves:
            new_st = deepcopy ( state )
            new_st.apply_move ( move, color )
            v = min ( v, self.__max_value ( e_color, new_st, alpha, beta, depth-1 ) )
            if v <= alpha:
                return v
            beta = min ( beta, v )
        
        return v
                          
    def eval ( self, board, who ):
        return evaluate ( board, who ) 
        
class Computer2 ( Computer ):
    def eval ( self, board, color ):
        return evaluate2 ( board, color ) 

class RandomPlayer ( Computer ):
    def get_move ( self ):
        x = random.sample ( self.current_board.get_valid_moves ( self.color ), 1 )    
        return x[0]
      
