from art import logo
from art import cards
from art import cards_value
from os import system
import random

def deal_card(user_cards, user_value):
    temp = random.randint(0,12)
    user_cards.append(cards[temp])
    user_value.append(cards_value[temp])

def calculate_score(user_value):
    if sum(user_value) == 21 and len(user_value) == 2:
        return 0
    if sum(user_value) > 21 and 11 in user_value:
        user_value.remove(11)
        user_value.append(1)
    return sum(user_value)

def compare(player, computer):
    if computer == 0:
        print('Computer has blackjack, you lost!')
    elif player == 0:
        print('You have blackjack, you won!')
    elif player > 21:
        print('You went over, you lost!')
    elif player <= 21 and computer > 21:
        print('Computer went over, you won!')
    elif player <= 21 and computer <= 21:
        print("Computer's score: " + str(computer))
        if player > computer:
            print('you won!')
        elif player < computer:
            print('you lost!')
        elif player == computer:
            print("It's a draw!")

def game():
    system('cls')
    print(logo)
    player_cards = []
    player_value = []
    computer_cards = []
    computer_value = []
    for i in range(2):
        deal_card(computer_cards,computer_value)
        deal_card(player_cards,player_value)
    
    print('Your card is: ', end= '')
    for cards in player_cards:
        print(cards, end = ' ')
    print("\nComputer's first card is ",end = '')
    for cards in computer_cards:
        print(cards, end = ' ')
    print('')
    #print(computer_cards[0])
    while True:
        player_score = calculate_score(player_value)
        computer_score = calculate_score(computer_value)
        if player_score == 0 or computer_score == 0:
            break
        else:
            cont = input('"hit" to draw another card, "stay" to stop: ')
            if cont == 'hit':
                deal_card(player_cards, player_value)
                print('Your cards now: ')
                for cards in player_cards:
                    print(cards, end = ' ')
                print('')
            else:
                break
    
    while computer_score < 17 and computer_score != 0:
        computer_score = calculate_score(computer_value)
        deal_card(computer_cards,computer_value)

    compare(player_score, computer_score)  
game()