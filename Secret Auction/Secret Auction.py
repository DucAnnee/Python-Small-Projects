from art import  logo
from os import system

print(logo + "\nWelcome to the secret auction program")
bid = {}
max = 0

while True:
    name = input('What is your name?: ')
    money = int(input('What is your bid?: $'))
    bid[name] = money
    confirm = input('Are there any other bidders? Type "yes" or "no". \n')
    if confirm == 'yes':
        system('cls')
        continue
    else:
        break

for bidder in bid:
    if bid[bidder] > max:
        max = bid[bidder]
        winner = bidder

print(f'The winner is {winner} with a bid of ${max}')       