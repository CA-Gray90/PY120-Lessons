class SpeedyMixin:
    def run_fast(self):
        self.speed = 70 # Mixins can initialize instance variables in methods other than init

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    DOG_YEARS = 7

    def __init__(self, name, age):
        self.dog_age = age * Dog.DOG_YEARS

class Greyhound(SpeedyMixin, Dog):
    pass

grey = Greyhound('Grey', 3)

'''
In this code snippet, the only instance variables that `grey` has are:
- self.dog_age

It doesn't have:
- self.name
- self.age

    This is because Dog defines its own __init__ method that doesn't initialize
    those variables even though it inherits from Animal which does.

It also doesn't have:
- self.speed

    This is because self.speed isn't initialized unless run_fast is invoked 
    even though it inherits from SpeedyMixin.
'''