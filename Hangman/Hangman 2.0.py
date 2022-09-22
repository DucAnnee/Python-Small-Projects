from logging import raiseExceptions
from turtle import clear
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
from os import system
import random



system('cls')
print(logo + 'Welcome to the hangman game!')

game_state = 1
while True:
    if game_state == 3:
        system('cls')
        print(logo + '\n')
        print('Thank you for playing the game!')
        break
    
    chosen_word = random.choice(word_list)
    answer = []
    for i in range(0,len(chosen_word)):
        answer += '_'
    lives = 6
    game_state = 1
    answered = []
    
    if game_state == 1:
        while game_state == 1:
            guess = input('Guess a letter: ').lower()
            system('cls')
            if len(guess) > 1:
                print('Please input only ONE letter!')
            else:    
                if guess in answered:
                    print(f'You already guessed {guess}!')
                answered.append(guess)
                if guess in chosen_word:
                    for i in range(len(chosen_word)):
                        if guess == chosen_word[i]:
                            answer[i] = guess
                else:
                    lives -= 1
                    print(f'{guess} is not in the word, you lost a life!')
                    print(f'{lives} lives remaining.')
                    if lives == 0:
                        game_state = 0
                for letter in answer:
                    print(letter, end= '')
                print(stages[lives])
                print('Guessed letters: ',end = '')
                for letter in answered:
                    print(letter, end = ' ')
            if '_' not in answer:
                game_state = 2
    if game_state == 0:
        print(f'\nYou lost! The word is "{chosen_word}"')
    else:
        print('You won!')
    cont = input('Do you want to continue? input "yes" or "no": ').lower()
    if cont == 'yes':
        system('cls')
        game_state = 1
    elif cont == 'no':
        game_state = 3 
    else:
        print('You must select "yes" or "no", please restart the game!')