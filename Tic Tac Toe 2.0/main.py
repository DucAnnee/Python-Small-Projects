from audioop import cross
from cmath import sqrt
import random
import sys
import pygame 
import copy
import numpy as np

from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)


class Board():
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.marked_sqrs = 0

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_square(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_sqrs.append( (row, col) )
        return empty_sqrs
    
    def is_full(self):
        return self.marked_sqrs == 9
    def state(self, show = False):
        #VERTICAL
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    win_colour = CIRC_COLOUR if self.squares[0][col] == 1 else CROSS_COLOUR
                    start_pos = (col * square_size + square_size // 2, 20)
                    end_pos = (col * square_size + square_size // 2, HEIGHT - 20)
                    pygame.draw.line(screen, win_colour, start_pos, end_pos, line_size)
                return self.squares[0][col]

        #HORIZONTAL
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    win_colour = CIRC_COLOUR if self.squares[0][col] == 1 else CROSS_COLOUR
                    start_pos = (20, row * square_size + square_size // 2)
                    end_pos = (WIDTH - 20, row * square_size + square_size // 2)
                    pygame.draw.line(screen, win_colour, start_pos, end_pos, line_size)
                return self.squares[row][0]

        #DESC DIAGONAL
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                win_colour = CIRC_COLOUR if self.squares[0][col] == 1 else CROSS_COLOUR
                pygame.draw.line(screen, win_colour, (20, 20), (WIDTH - 20, HEIGHT - 20), line_size)
            return self.squares[0][0]
        
        #ASC DIAGONAL
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            if show:
                win_colour = CIRC_COLOUR if self.squares[0][col] == 1 else CROSS_COLOUR
                pygame.draw.line(screen, win_colour, (20, HEIGHT - 20), (WIDTH - 20, 20), line_size)
                
            return self.squares[0][2]

        #DRAW
        return 0

class AI():
    def __init__(self, level = 1, player = 2):
        self.level = level
        self.player = player
    
    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        index = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[index]

    def minimax(self, board, max):
        case = board.state()
        if case == 1:
            return 1, None
            
        if case == 2:
            return -1, None

        elif board.is_full():
            return 0, None

        if max:
            max_eval = -100
            best_move = None
            for (row,col) in board.get_empty_sqrs():
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval             
                    best_move = (row,col)
            return max_eval, best_move

        elif not max:
            min_eval = 100
            best_move = None
            for (row,col) in board.get_empty_sqrs():
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval             
                    best_move = (row,col)
            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            eval = 'rnd'
            move = self.rnd(main_board)
        else:
            eval, move = self.minimax(main_board, False)
        print(f'AI chose to mark the square in pos {move} with an evaluation of {eval}.')
        return move

class Game():
    def __init__(self):
        self.board = Board()
        self.lines()
        self.ai = AI()
        self.gamemode = 'ai' #PvP or AI
        self.running = True
        self.player = 1 

    def change_mode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def make_move (self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()
    
    def is_over(self):
        return self.board.state(show = True) != 0 or self.board.is_full()

    def lines(self):
        screen.fill(BG_COLOUR)

        #VERTICAL 
        pygame.draw.line(screen, LINE_COLOUR, (square_size, 0), (square_size, HEIGHT),line_size)
        pygame.draw.line(screen, LINE_COLOUR, (WIDTH - square_size, 0), (WIDTH - square_size, HEIGHT),line_size)
        
        #HORIZONTAL
        pygame.draw.line(screen, LINE_COLOUR, (0, square_size), (WIDTH, square_size),line_size)
        pygame.draw.line(screen, LINE_COLOUR, (0, HEIGHT - square_size), (WIDTH, HEIGHT - square_size),line_size)

    def reset(self):
        self.__init__()

    def next_turn(self):
        self.player = self.player % 2 + 1 

    def draw_fig(self, row, col):
        if self.player == 1:
            start_pos_des = (col * square_size + cross_offset, row * square_size + cross_offset)
            end_pos_des = ((col +1) * square_size - cross_offset, (row + 1) * square_size - cross_offset)
            start_pos_asc = (col * square_size + cross_offset, (row + 1) * square_size - cross_offset)
            end_pos_asc = ((col +1) * square_size - cross_offset, row * square_size + cross_offset)
            pygame.draw.line(screen, CROSS_COLOUR, start_pos_des, end_pos_des, cross_size)
            pygame.draw.line(screen, CROSS_COLOUR, start_pos_asc, end_pos_asc, cross_size)
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
                    game.make_move(row, col)
                    if game.is_over():
                        game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_mode()
                    print(f'changed to {game.gamemode}')
                if event.key == pygame.K_r:
                    game.reset()
                    ai = game.ai
                    board = game.board
                if event.key == pygame.K_0:
                    ai.level = 0    
                if event.key == pygame.K_1:
                    ai.level = 1
        
        if game.gamemode == "ai" and game.player == ai.player and game.running:
            pygame.display.update()
            row, col = ai.eval(board)
            game.make_move(row, col)
            if game.is_over():
                    game.running = False
        pygame.display.update()
main()