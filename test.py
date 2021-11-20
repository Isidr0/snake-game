# from turtle import Turtle, Screen
#
# turtle = Turtle()
#
# turtle.heading()
#
# screen = Screen()
#
# screen.exitonclick()

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__() # Calling super in the subclass is recommended but not required.
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#
#     def swim(self):
#         print("moving in water.")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# think of a slice as slicing as beginning before the first item and after the second item.
# it makes sense to me to think about counting the commas and picturing the items between them as in the slice
# omit the second or first item after or before the colon to slice everything before or after the chosen item.
# the third digit defines step. so if you define 2 it will skip every other item. 2:5:2 would be ['c', 'e']
# use -1 for the increment to reverse the list [::-1]
# slice works for tuples as well

print(piano_tuple[2:5])
