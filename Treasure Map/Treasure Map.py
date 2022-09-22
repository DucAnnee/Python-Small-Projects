row1 = ['⬛️','⬛️','⬛️']
row2 = ['⬛️','⬛️','⬛️']
row3 = ['⬛️','⬛️','⬛️']
map = [row1, row2, row3]

for i in range(0,3):
    print(str(map[i]) + '\n')
print('Where do you want to put the treasure?')

pos = input().split()
y = int(pos[0])-1
x = int(pos[1])-1

map[x][y] = ' X'
for i in range(0,3):
    print(str(map[i]) + '\n')