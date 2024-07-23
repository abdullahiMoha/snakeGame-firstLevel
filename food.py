import turtle
from turtle import Turtle
import random


def rgb_colors():
	r = random.randint(0, 256)
	g = random.randint(0, 256)
	b = random.randint(0, 256)
	color = (r, g, b)
	return color


shapes = ["turtle", "circle", "square", "triangle", "classic"]


class Food(Turtle):
	""" This class created to manage food for the snake"""

	def __init__(self):
		"""Creating snake food"""
		super().__init__()
		self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		"""Puts the food into random location"""
		self.shape(random.choice(shapes))
		rand_x = random.randint(-280, 280)
		rand_y = random.randint(-280, 280)
		turtle.colormode(255)
		self.color(rgb_colors())
		self.goto(x = rand_x, y = rand_y)
