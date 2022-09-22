import random
print("Give me everybody's name, seperated by a comma.")
names = [x for x in input().split(', ')]
name = random.randint(0, len(names)-1)
print(name)
print(f"{names[name]} is going to pay the meal today!")