from color_mixin import ColorMixin

class Car(ColorMixin):
    def __init__(self, color):
        self.color = color
    
class House(ColorMixin):
    def __init__(self, color):
        self.color = color
    
class Light(ColorMixin):
    def __init__(self, color):
        self.color = color

car = Car('brown')
house = House('white')
light = Light('warm white')

print(car.color)
print(house.color)
print(light.color)

car.set_color('red')
print(f'Car is now {car.get_color()}')
house.set_color('blue')
print(f'House is now {house.get_color()}')
light.set_color('cool white')
print(f'Light is now {light.get_color()}')