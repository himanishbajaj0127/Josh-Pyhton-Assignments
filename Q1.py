'''Create animal base class with attribute and 
related methods then create sub concrete subclass 
using animal eg of subclass: cow, horse, dog'''

#The Animal class has a name and species attribute
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    #make_sound method that can be overridden by subclasses.
    def make_sound(self):
        pass

#Each subclass overrides the make_sound method to return a different sound
class Cow(Animal):
    def make_sound(self):
        return "Moo"

class Horse(Animal):
    def make_sound(self):
        return "Neigh"

class Dog(Animal):
    def make_sound(self):
        return "Bark"
