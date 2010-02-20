#!/usr/bin/env python
"""
othello.py Humberto Henrique Campos Pinheiro
Game initialization and main loop
 
"""

import time  
import ui
import player
import board
from config import BLACK, WHITE

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
        while True:
            if self.board.game_ended():
                break
            self.now_playing.get_current_board ( self.board )              
            if self.board.get_valid_moves( self.now_playing.color ) == []:
                self.now_playing, self.other_player = self.other_player, self.now_playing
                continue
            score, self.board = self.now_playing.get_move()
            whites, blacks, empty = self.board.count_stones()
            self.gui.update( self.board.board, blacks, whites )
            self.now_playing, self.other_player = self.other_player, self.now_playing

            # avoid 100% cpu load
            time.sleep( .005 )
             
        while True:
            self.gui.wait_quit()
            time.sleep ( .05 )
       

def main():
    game = Othello()
    game.run()

if __name__ == '__main__':
    main() 


