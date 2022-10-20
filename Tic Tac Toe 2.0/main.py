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
text_surface = font.render('Game draw!', False, (0, 0, 0))

class Board():
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
    def mark_square(self, row, col, player):
        self.squares[row][col] = player
    def empty_square(self, row, col):
        return self.squares[row][col] == 0

class Game():
    def __init__(self):
        self.board = Board()
        self.lines()
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
    def draw(self):
        temp = 0
        for i in range(len(self.board.squares)):
            if 0 in self.board.squares[i]:
                pass
            else:
                temp += 1
        if temp == 3:
            return True
        return False

def main():
    game = Game()
    board = game.board
    while True:
        if game.draw():
            screen.fill(BG_COLOUR)
            screen.blit(text_surface, dest=(10,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                col = pos[0] // square_size
                row = pos[1] // square_size
                print(row, col)
                if board.empty_square(row, col):
                    board.mark_square(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    print(board.squares)
        pygame.display.update()
main()