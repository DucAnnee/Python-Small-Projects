import random

def rock():
    print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
def paper():
    print("""
        _______
    ---'    ____)
            ______)
            _______)
            _______)
    ---.__________)
    """)
def scissors():
    print("""
        _______
    ---'   ____)
            ______)
        __________)
        (____)
    ---.__(___)
    """)
def image(n):
    if n == 0:
        rock()
    elif n == 1:
        paper()
    else:
        scissors()
def rule(a, b):
    if a == b:
        print('Draw!')
    elif a == 0 and b == 2:
        print('You win!')
    elif a == 2 and b == 0:
        print('You lose!')
    elif a > b:
        print('You win!')
    else:
        print('You lose!')

playerChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
computerChoice = random.randint(0,2)

image(playerChoice)
print(f'Computer chose: {computerChoice}')
image(computerChoice)

rule(playerChoice,computerChoice)