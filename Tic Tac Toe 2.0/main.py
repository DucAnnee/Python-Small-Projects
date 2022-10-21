import random
import sys
from turtle import bgcolor
import pygame 
import numpy as np

from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)
font = pygame.font.Font(pygame.font.get_default_font(), 100)
text_surface = font.render('Game draw!', False, (20, 140, 150))

class Board():
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
    def mark_square(self, row, col, player):
        self.squares[row][col] = player
    def empty_square(self, row, col):
        return self.squares[row][col] == 0
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_sqrs.append( (row, col) )
        return empty_sqrs
    def state(self):
        #VERTICAL
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        #HORIZONTAL
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        #DESC DIAGONAL
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[0][0]
        
        #ASC DIAGONAL
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            return self.squares[0][2]

        #DRAW
        return 0

class AI():
    def __init__(self, level = 0, player = 2):
        self.level = level
        self.player = player
    
    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        index = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[index]

    def eval(self, main_board):
        if self.level == 0:
            #random choice
            move = self.rnd(main_board)
        else:
            #minimax
            pass
        return move


class Game():
    def __init__(self):
        self.board = Board()
        self.lines()
        self.ai = AI()
        self.gamemode = 'ai' #PvP or AI
        self.running = True
        self.player = 1 
    def lines(self):
        #VERTICAL 
        pygame.draw.line(screen, LINE_COLOUR, (square_size, 0), (square_size, HEIGHT),line_size)
        pygame.draw.line(screen, LINE_COLOUR, (WIDTH - square_size, 0), (WIDTH - square_size, HEIGHT),line_size)
        #HORIZONTAL
        pygame.draw.line(screen, LINE_COLOUR, (0, square_size), (WIDTH, square_size),line_size)
        pygame.draw.line(screen, LINE_COLOUR, (0, HEIGHT - square_size), (WIDTH, HEIGHT - square_size),line_size)
    def next_turn(self):
        self.player = self.player % 2 + 1 
    def draw_fig(self, row, col):
        if self.player == 1:
            pygame.draw.line(screen, CROSS_COLOUR, (col*square_size + cross_offset, row*square_size + cross_offset),
                                                  ((col+1)*square_size - cross_offset, (row+1)*square_size - cross_offset), cross_size)
            pygame.draw.line(screen, CROSS_COLOUR, (col*square_size + cross_offset, (row+1) * square_size - cross_offset), 
                                                  ((col+1) * square_size - cross_offset, row * square_size + cross_offset), cross_size)
        if self.player == 2:
            pygame.draw.circle(screen, CIRC_COLOUR, (col * square_size + cir_offset, row * square_size + cir_offset), cir_radius, cir_size)

def main():
    game = Game()
    board = game.board
    ai = game.ai
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                col = pos[0] // square_size
                row = pos[1] // square_size
                if board.empty_square(row, col):
                    board.mark_square(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
        if game.gamemode == "ai" and game.player == ai.player:
            pygame.display.update()
            row, col = ai.eval(board)
            board.mark_square(row, col, game.player)
            game.draw_fig(row, col)
            game.next_turn()
        pygame.display.update()
main()