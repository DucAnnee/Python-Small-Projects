from distutils.core import setup
from turtle import Screen, Turtles
from constants import *

#INITIALIZING 
screen = Screen()
screen = setup(width = screen_width, height = screen_height)
screen.bgcolor(bg_colour)
screen.title('Snake Game')

segment_1 = Turtles('square')
segment_1.color('White')

segment_2 = Turtles('square')
segment_2.color('White')
segment_2.goto

segment_3 = Turtles('square')
segment_3.color('White')