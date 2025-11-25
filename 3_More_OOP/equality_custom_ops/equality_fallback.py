class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                print(f'Not the same animal! I am a {self.__class__.__name__}.')
                return NotImplemented
            print('Same animal. Comparing age...')
            return other.age == self.age

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __eq__(self, other):
        return self.age == other.age

fluffy = Cat('Fluffy', 3)
buster = Dog('Buster', 3)
cheddar = Cat('Cheddar', 3)

print(fluffy == buster)
# print(fluffy == cheddar)