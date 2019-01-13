""" Othello game GUI
    Humberto Henrique Campos Pinheiro
"""

import pygame
import sys
from pygame.locals import *
import time
from config import BLACK, WHITE, DEFAULT_LEVEL, HUMAN, COMPUTER
import os


class Gui:
    def __init__(self):
        """ Initializes graphics. """

        pygame.init()

        # colors
        self.BLACK = (0, 0, 0)
        self.BACKGROUND = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (128, 128, 0)

        # display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20)
        self.BOARD = (120, 40)
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # messages
        self.BLACK_LAB_POS = (5, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LAB_POS = (560, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Times New Roman", 22)
        self.scoreFont = pygame.font.SysFont("Serif", 58)

        # image files
        self.board_img = pygame.image.load(os.path.join(
            "res", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join(
            "res", "preta.bmp")).convert()
        self.white_img = pygame.image.load(os.path.join(
            "res", "branca.bmp")).convert()
        self.tip_img = pygame.image.load(os.path.join("res",
                                                      "tip.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("res",
                                                        "nada.bmp")).convert()

    def show_options(self):
        """ Shows game options screen and returns chosen options
        """
        # default values
        player1 = HUMAN
        player2 = COMPUTER
        level = DEFAULT_LEVEL

        while True:
            self.screen.fill(self.BACKGROUND)

            title_fnt = pygame.font.SysFont("Times New Roman", 34)
            title = title_fnt.render("Othello", True, self.WHITE)
            title_pos = title.get_rect(
                centerx=self.screen.get_width() / 2, centery=60)

            start_txt = self.font.render("Start", True, self.WHITE)
            start_pos = start_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=220)
            player1_txt = self.font.render("First Player", True, self.WHITE)
            player1_pos = player1_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=260)
            player2_txt = self.font.render("Second Player", True, self.WHITE)
            player2_pos = player2_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=300)
            level_txt = self.font.render("Computer Level", True, self.WHITE)
            level_pos = level_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=340)
            human_txt = self.font.render("Human", True, self.WHITE)
            comp_txt = self.font.render("Computer", True, self.WHITE)

            self.screen.blit(title, title_pos)
            self.screen.blit(start_txt, start_pos)
            self.screen.blit(player1_txt, player1_pos)
            self.screen.blit(player2_txt, player2_pos)
            self.screen.blit(level_txt, level_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if start_pos.collidepoint(mouse_x, mouse_y):
                        return (player1, player2, level)
                    elif player1_pos.collidepoint(mouse_x, mouse_y):
                        player1 = self.get_chosen_player()
                    elif player2_pos.collidepoint(mouse_x, mouse_y):
                        player2 = self.get_chosen_player()
                    elif level_pos.collidepoint(mouse_x, mouse_y):
                        level = self.get_chosen_level()

            pygame.display.flip()
            # desafoga a cpu

    def show_winner(self, player_color):
        self.screen.fill(pygame.Color(0, 0, 0, 50))
        font = pygame.font.SysFont("Courier New", 34)
        if player_color == WHITE:
            msg = font.render("White player wins", True, self.WHITE)
        elif player_color == BLACK:
            msg = font.render("Black player wins", True, self.WHITE)
        else:
            msg = font.render("Tie !", True, self.WHITE)
        self.screen.blit(
            msg, msg.get_rect(
                centerx=self.screen.get_width() / 2, centery=120))
        pygame.display.flip()

    def get_chosen_player(self):
        """ Asks for a player
        """
        while True:
            self.screen.fill(self.BACKGROUND)
            title_fnt = pygame.font.SysFont("Times New Roman", 34)
            title = title_fnt.render("Othello", True, Color(0, 0, 255))
            title_pos = title.get_rect(
                centerx=self.screen.get_width() / 2, centery=60)
            human_txt = self.font.render("Human", True, self.WHITE)
            human_pos = human_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=120)
            comp_txt = self.font.render("Computer", True, self.WHITE)
            comp_pos = comp_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=360)

            self.screen.blit(title, title_pos)
            self.screen.blit(human_txt, human_pos)
            self.screen.blit(comp_txt, comp_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if human_pos.collidepoint(mouse_x, mouse_y):
                        return HUMAN
                    elif comp_pos.collidepoint(mouse_x, mouse_y):
                        return COMPUTER

            pygame.display.flip()

    def get_chosen_level(self):
        """ Level options
        """

        while True:
            self.screen.fill(self.BACKGROUND)
            title_fnt = pygame.font.SysFont("Times New Roman", 34)
            title = title_fnt.render("Othello", True, self.BLUE)
            title_pos = title.get_rect(
                centerx=self.screen.get_width() / 2, centery=60)
            one_txt = self.font.render("Level 1", True, self.WHITE)
            one_pos = one_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=120)
            two_txt = self.font.render("Level 2", True, self.WHITE)
            two_pos = two_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=240)

            three_txt = self.font.render("Level 3", True, self.WHITE)
            three_pos = three_txt.get_rect(
                centerx=self.screen.get_width() / 2, centery=360)

            self.screen.blit(title, title_pos)
            self.screen.blit(one_txt, one_pos)
            self.screen.blit(two_txt, two_pos)
            self.screen.blit(three_txt, three_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if one_pos.collidepoint(mouse_x, mouse_y):
                        return 1
                    elif two_pos.collidepoint(mouse_x, mouse_y):
                        return 2
                    elif three_pos.collidepoint(mouse_x, mouse_y):
                        return 3

            pygame.display.flip()
            # desafoga a cpu
            time.sleep(.05)

    def show_game(self):
        """ Game screen. """

        # draws initial screen
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.BACKGROUND)
        self.score_size = 50
        self.score1 = pygame.Surface((self.score_size, self.score_size))
        self.score2 = pygame.Surface((self.score_size, self.score_size))
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_img, self.BOARD_POS,
                         self.board_img.get_rect())
        self.put_stone((3, 3), WHITE)
        self.put_stone((4, 4), WHITE)
        self.put_stone((3, 4), BLACK)
        self.put_stone((4, 3), BLACK)
        pygame.display.flip()

    def put_stone(self, pos, color):
        """ draws piece with given position and color """
        if pos == None:
            return

        # flip orientation (because xy screen orientation)
        pos = (pos[1], pos[0])

        if color == BLACK:
            img = self.black_img
        elif color == WHITE:
            img = self.white_img
        else:
            img = self.tip_img

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]

        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def clear_square(self, pos):
        """ Puts in the given position a background image, to simulate that the
        piece was removed.
        """
        # flip orientation
        pos = (pos[1], pos[0])

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(self.clear_img, (x, y), self.clear_img.get_rect())
        pygame.display.flip()

    def get_mouse_input(self):
        """ Get place clicked by mouse
        """
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    # click was out of board, ignores
                    if mouse_x > self.BOARD_SIZE + self.BOARD[0] or \
                       mouse_x < self.BOARD[0] or \
                       mouse_y > self.BOARD_SIZE + self.BOARD[1] or \
                       mouse_y < self.BOARD[1]:
                        continue

                    # find place
                    position = ((mouse_x - self.BOARD[0]) // self.SQUARE_SIZE), \
                               ((mouse_y - self.BOARD[1]) // self.SQUARE_SIZE)
                    # flip orientation
                    position = (position[1], position[0])
                    return position

                elif event.type == QUIT:
                    sys.exit(0)

            time.sleep(.05)

    def update(self, board, blacks, whites, current_player_color):
        """Updates screen
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        blacks_str = '%02d ' % int(blacks)
        whites_str = '%02d ' % int(whites)
        self.showScore(blacks_str, whites_str, current_player_color)
        pygame.display.flip()

    def showScore(self, blackStr, whiteStr, current_player_color):
        black_background = self.YELLOW if current_player_color == WHITE else self.BACKGROUND
        white_background = self.YELLOW if current_player_color == BLACK else self.BACKGROUND
        text = self.scoreFont.render(blackStr, True, self.BLACK,
                                     black_background)
        text2 = self.scoreFont.render(whiteStr, True, self.WHITE,
                                      white_background)
        self.screen.blit(text,
                         (self.BLACK_LAB_POS[0], self.BLACK_LAB_POS[1] + 40))
        self.screen.blit(text2,
                         (self.WHITE_LAB_POS[0], self.WHITE_LAB_POS[1] + 40))

    def wait_quit(self):
        # wait user to close window
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
