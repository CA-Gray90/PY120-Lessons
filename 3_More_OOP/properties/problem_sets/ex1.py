'''
Create a Person class with a "private" attribute _name. Use properties to
create a getter and setter for the _name attribute. The _name attribute must be
a string. Be sure to test your code.
'''

class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name given must be a string.')
        if name == '':
            raise ValueError('Name given cannot be an empty string')

        self._name = name

charles = Person('Charles')
print(charles.name) # Charles
charles.name = 'Paul'
print(charles.name) # Paul
charles.name = '' # ValueError
charles.name = 123 # TypeError