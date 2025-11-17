'''
Explain what the _cats_count variable is, what it does in this class, and how
it works. Write some code to test your theory
'''

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

'''
A:
The _cats_count variable is a class variable. It is a variable that is defined
in the class and is available within the class body, class methods, subclasses
and instances of the class.

What it does: It keeps a count of the instances that are instatiated by the class.
It does this in the __init__ method by calling self.__class__ which refers to the
class Cat, and using augmented assignment to assign the class variable _cats_count
to the value of itself + 1. This occurs every time a class instance is created.
'''

cat1 = Cat('type1')
cat2 = Cat('type2')
print(Cat.cats_count()) # 2
print(cat2.__class__.cats_count()) # 2
cat3 = Cat('type3')
print(Cat.cats_count()) # 3
cat4 = cat1
print(Cat.cats_count()) # 3. We didnt instantiate a new Cat object on line 35, just assigned cat4 to the same object as cat3
print(cat1 is cat4) # True