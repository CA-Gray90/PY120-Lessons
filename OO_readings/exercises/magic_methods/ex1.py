'''
- 3 instance variables: name, year, color
- str method that returns color capitalized year name
- repr method that returns Car(name, year, color)

'''

class Car:
    def __init__(self, id, year, color):
        self._id = id
        self._year = year
        self._color = color
    
    def __str__(self):
        return f'{self._color.capitalize()} {self._year} {self._id}'

    def __repr__(self):
        return f"Car({repr(self._id)}, {repr(self._year)}, {repr(self._color)})"


vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')