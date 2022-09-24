import os
from this import d
from turtle import update
os.system('cls')

class Board():
    def __init__(self):
        self.cells = [' ' for x in range(11)]

    def display(self):
        print(" %s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))
    
    def check_available(self, choice):
        return ' ' == self.cells[choice]

    def update(self, choice, cell_number):
        self.cells[cell_number] = choice

    def is_tie(self):
        for i in range(1, 10):
            if self.cells[i] == ' ':
                return False
        return True

    def is_win(self, choice):
        if self.cells[1] == choice and self.cells[2] == choice and self.cells[3] == choice:
            return True
        if self.cells[4] == choice and self.cells[5] == choice and self.cells[6] == choice:
            return True
        if self.cells[7] == choice and self.cells[8] == choice and self.cells[9] == choice:
            return True
        if self.cells[1] == choice and self.cells[5] == choice and self.cells[9] == choice:
            return True
        if self.cells[3] == choice and self.cells[5] == choice and self.cells[7] == choice:
            return True
        if self.cells[1] == choice and self.cells[4] == choice and self.cells[7] == choice:
            return True
        if self.cells[2] == choice and self.cells[5] == choice and self.cells[8] == choice:
            return True
        if self.cells[3] == choice and self.cells[6] == choice and self.cells[9] == choice:
            return True
        else:
            return False
board = Board()

def refresh():
    os.system('cls')
    print('Tic Tac Toe!')
    board.display()

def play(symbol):
    choice = int(input((f"[{symbol}'s turn] Choose a square (1 -> 9): ")))
    while board.check_available(choice) == False:
        refresh()
        choice = int(input((f"That square is occupied!\n[{symbol}'s turn] Choose a square (1 -> 9): ")))
    board.update(symbol, choice)
    refresh()
    if board.is_tie():
        print('Tied!')
        return True
    if board.is_win(symbol):
        print(f'{symbol} won!')
        return True

symbols = ['X', 'O']

while True:
    refresh()
    if play('X'):
        break
    if play('O'):
        break
