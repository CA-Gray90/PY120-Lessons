'''
Consider the following class that represents a value that can be either a
string or an integer

Assuming we have an expression like Silly(x) + y, the evaluation rules are as
follows:

    - If both x and y can be expressed as integers, compute the sum of the
    integer values of x and y.
    - Otherwise, concatenate the string values of x and y.

note:
A numeric string is a string that consists entirely of numeric digits. 
A non-numeric string is a string that contains at least one character that is 
not a numeric digit.
'''


class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

# Solution parts:
    def __add__(self, other):
        if not isinstance(other, (str, int)):
            return NotImplemented

        if str(self.value).isdigit() and str(other).isdigit():
            return Silly(int(self.value) + int(other))
        return Silly(str(self.value) + str(other))

    def __iadd__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Silly):
            return NotImplemented
        return str(self) == str(other)

    def __ne__(self, other):
        pass

print((Silly('abc') + 'def') == Silly('abcdef'))   # True
print((Silly('abc') + 123) == Silly('abc123'))     # True
print((Silly(123) + 'xyz') == Silly('123xyz'))     # True
print((Silly('333') + 123) == Silly(456))          # True
print((Silly(123) + '222') == Silly(345))          # True
print((Silly(123) + 456) == Silly(579))            # True
print((Silly('123') + '456') == Silly(579))        # True