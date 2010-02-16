#!/usr/bin/env python
"""
othello.py Humberto Henrique Campos Pinheiro
Game initialization and main loop
 
"""

import time  
import ui
import player
import board

BLACK = 1
WHITE = 2

class Othello:
    """ 
    Game main class.	
    """
	
    
    def __init__( self ):
        """ Show options screen and start game modules
        """

        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        
        # set up players
        player1, player2, level = self.gui.show_options()
        if player1 == "human":
            self.now_playing = player.Human ( self.gui, BLACK )
        else:
            self.now_playing = player.Computer ( BLACK, level+1 )
        if player2 == "human":
            self.other_player = player.Human ( self.gui, WHITE )
        else:
            self.other_player = player.Computer ( WHITE, level+1 )
                        
        self.gui.show_game()

    def run ( self ):
        """ Execute the game """

        quit = False

        # main loop
        while not quit:

            self.now_playing.get_current_board ( self.board )
            
            # Color positions            
            valid_moves = self.board.get_valid_moves( self.now_playing.color )
            
            for pos in valid_moves:
                self.gui.put_stone ( pos, "tip_color" )
                        
            if valid_moves == []:
		# there is no possible moves to this player, pass turn
                self.now_playing, self.other_player = \
                    self.other_player, self.now_playing
		# if opponent also cannot do moves the game is over
                valid_moves = self.board.get_valid_moves( self.now_playing.color )
                if valid_moves == []:
                    break
                continue
            # asks player to do a move
            while True:
                move = self.now_playing.get_move()            
                if move in valid_moves:
                    # ok, the move is valid
                    break
                            
            # update board
            self.board.apply_move ( move, self.now_playing.color )
            
            # update graphics
            board, n_blacks, n_whites = self.board.get_changes()
            self.gui.update ( board, n_blacks, n_whites )            
            
            # is the game ended?
            quit = self.board.game_ended()            

            # avoid 100% cpu load
            time.sleep( .05 )            

	    # erase helping move places
            for pos in valid_moves:
                if pos != move: 
                    self.gui.clear_square ( pos )
            
            # pass turn
            self.now_playing, self.other_player = \
                self.other_player, self.now_playing

        
        while True:
            self.gui.wait_quit()
            time.sleep ( .05 )



def main():
    game = Othello()
    game.run()

if __name__ == '__main__':
    main() 


