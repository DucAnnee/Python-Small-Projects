print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure')
stage1 = input("You're at a cross road. Where do you want to go? Select 'left' or 'right'\n")

if stage1 == "left":
    stage2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if stage2 == "wait":
        stage3 = input("You arrive at the treasure island. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if stage3 == "red":
            print('You found the treasure!')
        elif stage3 == "blue":
            print('You enter a room with full of beasts. Game over!')
        elif stage3 == "yellow":
            print('You enter a room full of toxic gas. Game over!')
    else:
        print('You chose to swim and drowned. Game over!')
else:
    print('You go into a jungle and die because of a spike trap. Game over!')