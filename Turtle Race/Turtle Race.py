from turtle import Turtle, Screen, TurtleScreen
import random

game_on = False

screen = Screen()
screen.setup(500, 400)

y_pos = [-75, -45, -15, 15, 45, 75]
colors = ['red', 'green', 'blue', 'purple', 'teal', 'orange']

selection = screen.textinput('Choose a turtle!','Which turtle would win the race? Pick a colour: ')
all_turtles = []

for index in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.up()
    turtle.color(colors[index])
    turtle.setpos(-240, y_pos[index])
    all_turtles.append(turtle)

if selection:
    game_on = True
while game_on:
    for turtle in all_turtles:
        current_x = turtle.xcor()
        if current_x > 230:
            game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == selection:
                print("You've won!")
            else:
                print("You've lost!")
            print(f"The {winning_colour} turtle is the winner!")
        temp = random.randint(0,10)
        turtle.forward(temp)


screen.exitonclick()
