'''
In the previous question, we had a mix-in called SpeedMixin that contained a
go_fast method. We add this mix-in to the Car class as shown below:
'''

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast()
# I am a super fast Car!

'''
When we called small_car.go_fast, you may have noticed that the output includes
the vehicle type. How is this done?
'''

'''
This is done calling self.__class__.__name__
self refers to the object calling the method, class is the class of the object,
in this case a car, and name returns the name of the class as a string.
'''