class Octopus:
    # instance variables / attributes
    def __init__(self, colour, pattern):
        self.num_of_legs = 8
        self.colour = colour
        self.pattern = pattern
        self.speed = 0

    # methods
    def up(self):
        print("swimming up")
        self.speed += 1

    def down(self):
        print("swimming down")

    def sideways(self):
        print("swimming to the side")

    def turn(self):
        print("spinning!")

    def change_colour(self, newColour):
        self.colour = newColour

# for main
"""
from octopus import Octopus

inky = Octopus("purple", "stripes")
sally = Octopus("green", "polka dots")

print(inky.colour)
print(inky.num_of_legs)
print(inky.pattern)

inky.up()
inky.down()
inky.sideways()
inky.turn()

inky.change_colour("blue")

print(inky.colour)

print(sally.colour)
print(sally.pattern)

"""
