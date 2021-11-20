from turtle import Turtle
import random


class Food(Turtle): # The Turtle superclass is in the parens

    def __init__(self):
        """Generate food. Small blue circle."""
        super().__init__() # the super method calls the Turtle class init method inside the Food init method.
        # these are all turtle methods.
        # all of this will happen when you initialize an object from the food class (instantiate?)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Randomly move food to new location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)