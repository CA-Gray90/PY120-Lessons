class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __lt__(self, other):              # Uncomment and delete __lt__ in Cat?
    #     print('Pet knows how to compare')
    #     return self.age < other.age

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __lt__(self, other):
        print('Cat doesnt know how to compare')
        return NotImplemented

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __lt__(self, other):
        print('Dog knows how to compare (lt)')
        return self.age < other.age

    def __gt__(self, other):
        print('Dog knows how to compare (gt)')
        return self.age > other.age

cat1 = Cat('Cheddar', '3')
dog1 = Dog('Buster', '4')

# Compare by age
print(cat1 < dog1) 
# Cat doesn't know, dog knows
# Tries a.__lt__(b) -> returns NotImplemented
# Then tries b.__gt__(a) -> returns True