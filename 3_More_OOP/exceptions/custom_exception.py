'''
Define a class Cat and a class Dog that both inherit from Animal.
Define an instance method in Animal called `reproduce`. 
In this method, we must check that both objects are of the same species,
otherwise raise a custom error. If they are both of the same species (aka class)
return a new object of that class with the name 'Baby {ClassName}' with an age
of 0.

write some examples that checks your code works
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def reproduce(self, other):
        if not isinstance(other, type(self)):
            raise SpeciesError
        print(f'{self.name} and {other.name} had a baby!')
        return self.__class__(f'Baby {self.__class__.__name__}', 0)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class SpeciesError(Exception):
    def __init__(self, message='Incompatible species, cannot breed.'):
        super().__init__(message)

cat1 = Cat('Fluffy', 6)
cat2 = Cat('Harry', 10)
dog1 = Dog('Millie', 3)
dog2 = Dog('Buck', 5)

cat3 = cat1.reproduce(cat2)
print(cat3.name, cat3.age) # baby cat 0
dog3 = dog1.reproduce(dog2)
print(dog3.name, dog3.age) # baby dog 0

abomination = cat1.reproduce(dog1) # Raise custom error