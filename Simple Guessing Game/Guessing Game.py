import random
answer = random.randint(1, 20)
print(answer)
count = 0
check = False
while count <= 6:
    n = int(input("Input a number between 1 to 20: "))
    if n == answer:
        print('Congratulation! You won the game')
        check = True
        break
    else:
        if abs(n-answer) > 15:
            print('guess is so far away try again')
        elif 10 < abs(n-answer) <= 15:
            print('guess is far away try again')
        elif 5 < abs(n-answer) <= 10:
            print('guess is close try again')
        elif 1 <= abs(n-answer) <= 5:
            print('guess is so close try again')
        count+=1
if check == False:
    print('You Lost the Game! Thank you for using my guessing game.')