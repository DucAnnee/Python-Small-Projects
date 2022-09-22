heights = input('Input a list of student heights: ').split()
sum = 0
for height in heights:
    sum += int(height)

num = 0
for height in heights:
    num += 1

average = round(sum/num)

print(f"The average height is {average}")