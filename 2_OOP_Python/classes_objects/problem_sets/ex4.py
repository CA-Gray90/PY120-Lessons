# 4
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'.strip() # Computes the name dynamically
    
    @name.setter
    def name(self, name):
        names = name.split()
        self.first_name = names[0]
        self.last_name = names[1] if len(names) > 1 else ''

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

# Test:
bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob.name == rob.name)