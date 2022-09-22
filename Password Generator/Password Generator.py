import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = int(input('How many Letters would you like in your password?\n'))
symbol = int(input('How many Symbols would you like in yuor password?\n'))
number = int(input('How many Numbers would you like in your password?\n'))

password = []

for i in range(letter):
    password.append(letters[random.randint(0,len(letters)-1)])
for i in range(symbol):
    password.append(symbols[random.randint(0,len(symbols)-1)])  
for i in range(number):
    password.append(numbers[random.randint(0,len(numbers)-1)])    

random.shuffle(password)
print('You password is: ', end = '')
for i in password:
    print(i, end = '')