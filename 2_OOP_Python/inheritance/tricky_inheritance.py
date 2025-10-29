class Cat:
    counter = 0

    def __init__(self):
        self.__class__.counter += 1  # augmented assignment statement
#       self.__class__.counter = self.__class__.counter + 1
#       GoodCat.counter = GoodCat.counter + 1
#       GoodCat.counter = 0 + 1
#
      

class GoodCat(Cat):
    pass

# can you prove that the counter var on Cat is the same as the counter var accessed by GoodCat

print(Cat.__init__ is GoodCat.__init__)
GoodCat.__init__ = 0
print(Cat.__init__ is GoodCat.__init__)
# print(GoodCat.counter)  # 0
print(vars(GoodCat))    # why is `counters` missing?
a_cat = GoodCat()
print(vars(GoodCat))

# print(Cat.counter)      # 0
# print(GoodCat.counter)  # 1

print(GoodCat.mro())

"""
How are things inherited?
    - class var
    - class method
    - instance var
    - instance methods
"""