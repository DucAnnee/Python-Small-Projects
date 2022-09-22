import random
from logging import raiseExceptions
from os import system
from art import logo

def set_difficulty():
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if difficulty == 'easy':
        print('You have 10 tries!')
        lives = 10
    elif difficulty == 'hard':
        print('You have 5 tries!')
        lives = 5
    return lives

def check_answer(answer, guess, lives):
    if guess > answer:
        print('Too high!')
        return lives - 1
    elif guess < answer:
        print('Too low!')
        return lives - 1
    elif guess == answer:
        print('You got it! Congratulation!')
        return lives - lives -1

def game():
    system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    lives = set_difficulty()
    answer = random.randint(1,100)
    while lives > 0:
        guess = int(input('Make a guess: '))
        lives = check_answer(answer, guess, lives)
        if lives > 0:
            print(f'You have {lives} attempt(s) left!')
    if lives == 0:
        print('You lost!')
game()