import random
from data import data
from art import logo
from art import vs
from os import system

def get_option():
    return random.choice(data)

def compare(guess, followers_A, followers_B):
    if followers_A > followers_B:
        return guess == 'A'
    else:
        return guess == 'B'

def display(option):
    name = option['name']
    description = option['description']
    country = option['country']
    return f'{name}, a {description}, from {country}'

def game():
    print(logo)
    point = 0
    should_continue = True
    optionA = get_option()
    optionB = get_option()

    while should_continue == True:
        optionA = optionB
        optionB = get_option()

        while optionB == optionA:
            optionB = get_option()

        print(f'Compare A: {display(optionA)}')
        print(vs)
        print(f'Against B: {display(optionB)}')

        followers_A = optionA['follower_count']
        followers_B = optionB['follower_count']

        guess = input("Who has more followers? Type 'A' or 'B': ")

        system('cls')
        print(logo)

        if compare(guess, followers_A, followers_B):
            point += 1
            print(f'Correct! Your current score is {point}')
        else:
            print(f'Incorrect! Your final score is {point}')
            break

game()