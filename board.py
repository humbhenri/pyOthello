#!/usr/bin/env python
""" game.py Humberto Henrique Campos Pinheiro
Este arquivo implementa a logica do jogo Othello
""" 


BLACK = 1
WHITE = 2

class Board:
    """ Rules of the game """

    def __init__ ( self ):              
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.black_pieces = 2
        self.white_pieces = 2 
        self.board = [ [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0] ]
        self.board[3][4] = self.BLACK
        self.board[4][3] = self.BLACK
        self.board[3][3] = self.WHITE
        self.board[4][4] = self.WHITE
        self.valid_moves = []  
    
    def __getitem__ ( self, i, j):
        return self.board[i][j]
    
    def lookup ( self, row, column, color ):        
	""" Returns the possible positions that there exists at least one straight
	(horizontal, vertical, or diagonal) line between the piece specified by (row,
	column, color) and another piece of the same color."""
        
        if color == self.BLACK:
            other = self.WHITE
        else:
            other = self.BLACK

        places = []
                
        if ( row < 0 or row > 7 or column < 0 or column > 7 ):
            return places            

	# For each direction search for possible positions to put a piece.

        # north
        i = row - 1
        if ( i >= 0 and self.board[i][column] == other ):
            i = i - 1            
            while ( i >= 0 and self.board[i][column] == other ):
                i = i - 1                
            if ( i >= 0 and self.board[i][column] == 0 ):
                places = places + [( i, column)]

        # northeast
        i = row - 1
        j = column + 1
        if ( i >= 0 and j < 8 and self.board[i][j] == other ) :
            i = i - 1
            j = j + 1
            while (  i >= 0 and j < 8 and self.board[i][j] == other ):
                i = i - 1
                j = j + 1
            if ( i >= 0 and j < 8 and self.board[i][j] == 0 ):
                places = places + [(i, j)]

        # east
        j = column + 1
        if ( j < 8 and self.board[row][j] == other ) :
            j = j + 1
            while ( j < 8 and self.board[row][j] == other ):
                j = j + 1
            if ( j < 8 and self.board[row][j] == 0 ):
                places = places + [(row, j)]

        # southeast
        i = row + 1
        j = column + 1        
        if ( i < 8 and j < 8 and self.board[i][j] == other ) :
            i = i + 1
            j = j + 1
            while (  i < 8 and j < 8 and self.board[i][j] == other ):
                i = i + 1
                j = j + 1
            if ( i < 8 and j < 8 and self.board[i][j] == 0 ):
                places = places + [(i, j)]

        # south
        i = row + 1
        if ( i < 8 and self.board[i][column] == other ):
            i = i + 1
            while ( i < 8 and self.board[i][column] == other ):
                i = i + 1
            if ( i < 8 and self.board[i][column] == 0 ):
                places = places + [(i, column)]

        # southwest
        i = row + 1
        j = column - 1
        if ( i < 8 and j >= 0 and self.board[i][j] == other ):
            i = i + 1
            j = j - 1
            while ( i < 8 and j >= 0 and self.board[i][j] == other ):
                i = i + 1
                j = j - 1
            if ( i < 8 and j >= 0 and self.board[i][j] == 0 ):
                places = places + [(i, j)]

        # west
        j = column - 1
        if ( j >= 0 and self.board[row][j] == other ):
            j = j - 1
            while ( j >= 0 and self.board[row][j] == other ):
                j = j - 1
            if ( j >= 0 and self.board[row][j] == 0 ):
                places = places + [(row, j)]

        # northwest
        i = row - 1
        j = column - 1
        if ( i >= 0 and j >= 0 and self.board[i][j] == other):
            i = i - 1
            j = j - 1
            while ( i >= 0 and j >= 0 and self.board[i][j] == other):
                i = i - 1
                j = j - 1
            if ( i >= 0 and j >= 0 and self.board[i][j] == 0 ):
                places = places + [(i, j)]

        return places


    def get_valid_moves ( self, color ):        
	""" Get the avaiable positions to put a piece of the given color. For each
	piece of the given color we search its neighbours, searching for pieces of the 
	other color to determine if is possible to make a move. This method must be 
	called before apply_move."""
        
        if color == self.BLACK:
            other = self.WHITE
        else:
            other = self.BLACK

        places = []

        for i in range ( 8 ) :
            for j in range ( 8 ) :
                if self.board[i][j] == color :
                    places = places + self.lookup ( i, j, color )
        
        places = list( set ( places ))
        self.valid_moves = places
        return places


    def apply_move ( self, move, color ):        
	""" Determine if the move is correct and apply the changes in the game.
	"""

        # test if the move is correct
        if move in self.valid_moves:                        
            self.board[move[0]][move[1]] = color                     
            for i in range ( 1, 9 ):
                self.flip ( i, move, color )

        # update counters
        self.black_pieces = 0
        self.white_pieces = 0
        for row in self.board:
            for piece in row:
                if piece == self.BLACK:
                    self.black_pieces += 1
                elif piece == self.WHITE:
                    self.white_pieces += 1
                
                    
    def flip ( self, direction, position, color ):        
	""" Flips (capturates) the pieces of the given color in the given direction
	(1=North,2=Northeast...) from position. """
        
        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        elif direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        elif direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        elif direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        elif direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        elif direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        elif direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        elif direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1
        
        places = []     # pieces to flip
        i = position[0] + row_inc
        j = position[1] + col_inc 

        if color == self.WHITE:
            other = self.BLACK
        else:
            other = self.WHITE
        
        if  i in range( 8 ) and j in range( 8 ) and self.board[i][j] == other:
            # assures there is at least one piece to flip
            places = places + [(i,j)]
            i = i + row_inc
            j = j + col_inc
            while i in range( 8 ) and j in range( 8 ) and self.board[i][j] == other:
                # search for more pieces to flip
                places = places + [(i,j)]
                i = i + row_inc
                j = j + col_inc
            if i in range( 8 ) and j in range( 8 ) and self.board[i][j] == color:
                # found a piece of the right color to flip the pieces between
                for pos in places:
                    # flips
                    self.board[pos[0]][pos[1]] = color
                       

       
    def get_changes ( self ):
	""" Return black and white counters. """
        
        blacks, whites = self.count_stones()

        return ( self.board, blacks, whites )


    def game_ended ( self ):
        """ Is the game ended? """

        # if board is full or it's not possible to do moves anymore
        # the game is over, the winner is the one with more pieces
        for row in self.board:
            for stone in row:
                if stone == 0:
                    # there is still a empty place
                    return False

        return True
        

    def print_board ( self ):
        """ Print the board: B - black, W - white, E - empty"""

        for i in range ( 8 ):
            print i, ' |',
            for j in range ( 8 ):                
                if self.board[i][j] == self.BLACK:
                    print 'B',
                elif self.board[i][j] == self.WHITE:
                    print 'W',
                else:
                    print 'E',
                print '|',
            print 


    def count_stones ( self ):
        """ Returns counters
        """
        return ( self.black_pieces, self.white_pieces )

