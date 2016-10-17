"""
Name: Jeron Amory
Email: j.amory268@gmail.com
Assignment: Homework 3 - OOP Repeat
Due: 17 October @ 1:00 p.m.
"""


class Skittle(object):
    """A Skittle object has a color to describe it."""
    def __init__(self, color):
        self.color = color

class Bag(object):
    """A Bag is a collection of Skittles. All bags share the
    number of Bags ever made (sold) and each bag keeps track of
    its Skittles in a list.
    """

    number_sold = 0

    def __init__(self):
        self.skittles = []
        Bag.number_sold += 1
        

    def tag_line(self):
        """Print the Skittles tag line."""
        print("Taste the rainbow!")

    def print_bag(self):
        print([s.color for s in self.skittles])

    def take_skittle(self):
        """Take the first skittle in the bag (from the front of
        the skittles list).
        """
        return self.skittles.pop(0)

    def add_skittle(self, s):
        """Add a skittle to the bag."""
        self.skittles.append(s)
        
    def take_color(self, color):
	"""takes a color and removes (and returns) 
	a Skittle of that color from the bag
	"""
    	for color in self.skittles:
    		return self.Skittle(self.color).pop(0)
    	
    def take_all(self):
	"""takes all the Skittles in the current bag and prints 
	the color of the each Skittle taken from the bag.
	"""
    	return self.take_skittle()
    	

        
"""
Answer 1
"""

johns_bag = Bag()
johns_bag.print_bag()
#johns_bag.print_bag() prints an empty list []

for color in ['blue', 'red', 'green', 'red']:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
#johns_bag.print_bag() now prints: ['blue', 'red', 'green', 'red']

s = johns_bag.take_skittle()
print(s.color)
#since the 1st skittle in the bag is returns, prints: blue

print(johns_bag.number_sold)
#one skittle was taken from the bag, so prints: 1

print(Bag.number_sold)
#since 1 was sold, prints: 1

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
#since a red, green, and red skittle remain, prints: ['red', 'green', 'red']
#prints: none 

print(Bag.number_sold)
#prints: 2

print(soumyas_bag.number_sold)
#prints: 2

kays_bag = Bag()
print(kays_bag.take_color("green"))
kays_bag.add_skittle("purple")
print(kays_bag.take_all())


"""
Answer 2
"""


def take_color(self, color):
    	for color in self.skittles:
    		return self.Skittle(self.color).pop(0)

    	
    	
"""
Answer 3
"""

def take_all(self):
	return self.take_skittle()
