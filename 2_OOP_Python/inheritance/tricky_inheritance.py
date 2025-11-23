# class Cat:
#     counter = 0

#     def __init__(self):
#         self.__class__.counter += 1  # augmented assignment statement
# #       self.__class__.counter = self.__class__.counter + 1
# #       GoodCat.counter = GoodCat.counter + 1
# #       GoodCat.counter = 0 + 1
# #
      

# class GoodCat(Cat):
#     pass

# # can you prove that the counter var on Cat is the same as the counter var accessed by GoodCat

# print(Cat.__init__ is GoodCat.__init__)
# GoodCat.__init__ = 0
# print(Cat.__init__ is GoodCat.__init__)
# # print(GoodCat.counter)  # 0
# print(vars(GoodCat))    # why is `counters` missing?
# a_cat = GoodCat()
# print(vars(GoodCat))

# # print(Cat.counter)      # 0
# # print(GoodCat.counter)  # 1

# print(GoodCat.mro())

"""
How are things inherited?
    - class var
    - class method
    - instance var
    - instance methods
"""

# class Cat:
#     counter = 0

#     def __init__(self):
#         self.__class__.counter = self.__class__.counter + 1

# class GoodCat(Cat):
#     pass

# a_cat = GoodCat()

# print(Cat.counter)      # 0
# print(GoodCat.counter)  # 1

# class Vehicle:
#     WHEELS = 4

#     @classmethod
#     def number_of_wheels(cls):
#         return cls.WHEELS

# class Motorcycle(Vehicle):
#     WHEELS = 2

# print(Motorcycle.number_of_wheels()) # 2
# print(Vehicle.number_of_wheels())    # 4

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Dog(Animal):
    def __init__(self, name):
        # This line ensures the Animal.__init__ method is called
        # super().__init__(name)
        pass

    def speak(self):
        # self.name is available here because super().__init__ was called
        return f'bark! bark! {self.name} bark! bark!'

teddy = Dog('Teddy')

# Calling an inherited instance method
print(teddy.get_name())      # AttributeError: name not defined

# Calling a method on the subclass that uses an "inherited" instance variable
print(teddy.speak())         # Attribute error: name not defined