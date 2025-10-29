# 1:
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# Test:
bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert

'''
In this example, I've defined a class `Person`. When we initialize an instance of `Person` we require an argument for `name`.
I also have defined a getter and setter method using the @property decorator for the `name` instance variable. This 
gives `Person` one property and allows for accessing and setting this instance variable using syntax similar to accessing 
an object attribute.
'''