# 2:
class Person:
    def __init__(self, first, last=''):
        self.first_name = first
        self.last_name = last

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'.strip() # Get rid of any whitespace if no last name

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

'''
In this code snippet, we have defined a class `Person` with 3 properties, `name`, `first_name` and `last_name`. We first instantiate
an instance of `Person` assigning it to `bob` and passing in 'Robert' as the first name. We don't pass a second argument and so the `last_name`
instance variable gets assigned to the default value `''`. We then access the `name`, `first_name` and `last_name` properties. Finally,
we invoke the setter method for `last_name` which assigns `'Smith'` to the `_last_name` instance variable.
`bob.name` accesses the `name` property at the end which now returns 'Robert Smith'.
'''