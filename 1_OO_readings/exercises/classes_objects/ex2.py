class Person:

    @staticmethod
    def validate_name(first, last):
        if first.isalpha() and last.isalpha():
            return True
        else:
            raise ValueError('Names must be alphabetic characters only.')

    def __init__(self, first, last):
        if self.__class__.validate_name(first, last):
            self._first = first
            self._last = last

    @property
    def name(self):
        return f'{self._first.capitalize()} {self._last.capitalize()}'

    @name.setter
    def name(self, name):
        if self.__class__.validate_name(*name):
            self._first = name[0]
            self._last = name[1]

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

# Second attempt:
'''
P:
Create a Person class with two instance variables to hold a person's first an
last names. The names should be passed to the constructor as arguments and stored
separately. The first and last names are required and must consist entirely of
alphabetic characters.

The class should also have a getter method that returns the person's name as a
full name (the first and last names are separated by spaces), with both first
and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element
tuple. These names must meet the requirements given for the constructor.


'''

class Person:

    @staticmethod
    def validate_name(name):
        return name.isalpha()

    def __init__(self, first_name, last_name):
        if self.__class__.validate_name(first_name) and \
            self.__class__.validate_name(last_name):
            self._first_name = first_name
            self._last_name = last_name
        else:
            raise ValueError('Names must be alphabetic characters')
        
    @property
    def name(self):
        return f'{self._first_name.capitalize()} {self._last_name.capitalize()}'
    
    @name.setter
    def name(self, names):
        if len(names) != 2:
            raise ValueError('Only 2 names must be given.')
        
        first, last = names

        if self.__class__.validate_name(first) and \
            self.__class__.validate_name(last):
            self._first_name = first
            self._last_name = last
        else:
            raise ValueError('Names must be alphabetic characters')