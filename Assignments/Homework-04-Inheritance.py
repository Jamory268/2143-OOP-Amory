"""
Name: Jeron Amory
Email: j.amory268@gmail.com
Assignment: Homework-04-Inheritance
Due: 24 October @ 1:00 p.m.
"""

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print("...")
        
class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print("woof!")
        
        
#Answer 1
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
    	Pet.__init__(self, name, owner)
    	self.lives = 9



    def talk(self):
        """A cat says meow! when asked to talk."""
        print("meow!")




    #def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        if self.lives > 0:
        	self.lives = self.lives - 1
        else:
        	self.is_alive = False
        
#Answer 2   
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# prints 4

print(b.a)
# prints 3

#print(f.garply())
# prints what ?

print(b.garply())
# prints 3

b.a = 9
print(b.garply())
# prints 9

f.baz = lambda val: val * val
print(f.garply())
# prints 16
