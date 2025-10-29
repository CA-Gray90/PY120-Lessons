'''
P:
Create a Car class that meets these requirements:

    Each Car object should have a model, model year, and color provided at instantiation time.
    You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
    Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off.
        Each method should display an appropriate message.
    Create a method that prints a message about the car's current speed.
    Write some code to test the methods.

'''

class Car:
    COLORS = ['red', 'blue', 'black', 'white', 'silver', 'grey', 'green',
              'yellow']

    @staticmethod
    def get_mileage(gallons, distance):
        mileage = distance / gallons
        print(f'Mileage of car is {mileage}')

    def __init__(self, model, model_year, color):
        self._model = model
        self._model_year = model_year
        self._color = color
        self._current_speed = 0
        self._engine_state = False

        print(f'{self._color} {self._model_year} {self._model} '
              'has been initialized.')

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._model_year
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if color.lower() in Car.COLORS:
            self._color = color
        else:
            print('The car does not come in that color')

    def spray_color(self, new_color):
        self.color = new_color
        print(f'Car has been sprayed a new color! It is now {self.color}')
    
    def engine_on(self):
        if self._engine_state:
            print('Attempted to turn on engine: Engine already on!')
        else:
            print(f'{self._model} has turned on')
            self._engine_state = True
    
    def accelerate(self):
        if self._engine_state:
            print(f'{self._model} is accelerating')
            self._current_speed += 1
        else:
            print('Accelerator applied: Car must be switched on first')
    
    def brake(self):
        if self._current_speed > 0:
            print(f'{self._model} is braking')
            self._current_speed -= 1
        else:
            print(f'Brake pedal pressed: car is already at a standstill')
        
    def engine_off(self):
        if self._engine_state and self._current_speed == 0:
            print(f'{self._model} has switched off')
            self._engine_state = False
        elif self._current_speed != 0:
            print('Attempted to switch off engine: '
                  'Bring vehicle to a stop before switching off engine')
        else:
            print('Attempted to switch off engine: Engine is already off')
    
    def current_speed(self):
        print(f'Current speed: {self._current_speed}')

car = Car('Ford', '1992', 'Red')

print(f'Car is a {car.model}')
print(f'Car is {car.color}')
car.color = 'Blue'
print(f'Car is now {car.color}')
car.color = 'Purple'
car.spray_color('green')
car.engine_on()
car.accelerate()
car.accelerate()
car.accelerate()
car.brake()
car.current_speed() # 2
car.brake()
car.current_speed() # 1
car.brake()
car.engine_off()
car.get_mileage(4, 120)