# 3
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
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

'''
In this code snippet, we now have a `name` setter that has been defined. In this
setter method, we first get a list of the names from the `name` argument provided.
We then assign the first element in `names` to the `_first_name` property using
the `first_name` setter. Then, if there is a second name present, we assign that
name to `_last_name` using the `last_name` setter. If there is no last name
present, `_last_name` gets assigned to `''`. When the `name` property is called,
it computes the full name dynamically, concatenating the first name and last name
together with a space inbetween and returning it.
'''