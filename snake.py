from turtle import Turtle, colormode
import random

# Setting positions for snake segments to be placed on as well as a color list to change each additional segment
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
colormode(255)
color_list = [(172, 43, 53), (218, 213, 124), (104, 155, 117), (240, 246, 243), (103, 169, 225), (128, 18, 34),
              (199, 153, 75), (173, 142, 188), (3, 153, 171), (44, 42, 40), (1, 52, 91), (121, 119, 160),
              (239, 242, 247), (77, 176, 97)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_head()
        self.create_snake()
        self.head = self.segments[0]

    def create_head(self):
        random_color = random.choice(color_list)
        head = Turtle("triangle")
        head.color(random_color)
        head.penup()
        head.goto(0, 0)
        self.segments.append(head)

    def create_snake(self):
        for position in STARTING_POSITIONS[1:]:
            self.add_segment(position)

    def add_segment(self, position):
        random_color = random.choice(color_list)
        new_segment = Turtle("square")
        new_segment.color(random_color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_head()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): # range(start: , Stop: , step: )
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
