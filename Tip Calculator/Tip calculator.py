print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
num = int(input('How manh people to split the bill? '))

tip = bill * percentage / 100
total = bill + tip
pay = round(total/num, 2)

print(f'Each person should pay: ${pay}')