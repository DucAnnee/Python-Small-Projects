from logging import raiseExceptions
from art import art
from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def check_ingredients(order):
    for item in MENU[order]['ingredients']:
        if resources[item] < MENU[order]['ingredients'][item]:
            print(f'Sorry, there is not enough {item}')
            return False
    return True

def count_money():
    print('Please insert coins.')
    total = int(input('How may quarters?: ')) * 0.25
    total += int(input('How may dimes?: ')) * 0.1 
    total += int(input('How may nickels?: ')) * 0.05
    total += int(input('How may pennies?: ')) * 0.01
    return total

def check_money(money, order):
    if money < MENU[order]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money == MENU[order]['cost']:
        print("Thank you for purchasing, please wait a moment.")
        return True
    elif money > MENU[order]['cost']:
        change = round(money - MENU[order]['cost'],2)
        print("Thank you for purchasing, please wait a moment.")
        print(f"Here is ${change} in change")
        return True

def brew(order):
    for item in MENU[order]['ingredients']:
        resources[item] -= MENU[order]['ingredients'][item]
    
def report():
    global profit
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit}')

def coffee_machine():
    global profit
    print(art)
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'off':
            print('Coffee machine is off, ready for maintance')
            break
        elif order == 'report':
            report()
        elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
            if check_ingredients(order):
                money = count_money()
                if check_money(money, order):
                    profit += MENU[order]['cost']
                    brew(order)
                    sleep(1)
                    print(f'Here is your {order}, enjoy!')
                else:
                    break
        else:
            raiseExceptions('You can only select one of the three options!')

coffee_machine()