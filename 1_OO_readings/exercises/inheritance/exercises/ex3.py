class Vehicle:
    vehicle_number = 0

    @classmethod
    def vehicles(cls):
        return cls.vehicle_number

    def __init__(self):
        Vehicle.vehicle_number += 1

class SignalMixin:
    def signal_left(self):
        print('Signalling left')
    
    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Car(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()

class Truck(SignalMixin, Vehicle):
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    def __init__(self):
        super().__init__()

# car1 = Car()
# truck1 = Truck()
# boat1 = Boat()

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# # AttributeError: 'Boat' object has no attribute
# # 'signal_left'

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())
