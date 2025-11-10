'''
Create a Car class that has a class variable named manufacturer and an instance
variable named manufacturer. Initialize these variables to different values.
Add a show_manufacturer method that prints both the class and instance variables.
'''

class Car:
    manufacturer = 'Mercedes Benz'

    def __init__(self):
        self.manufacturer = 'Toyota'
    
    def show_manufacturer(self):
        return f'{self.__class__.manufacturer=} {self.manufacturer=}' # Mercedes Bez, Toyota

car = Car()
print(car.show_manufacturer())