'''
Suppose you have the Oracle class from above and a RoadTrip class that inherit
 from the Oracle class, as shown below:
'''

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]
    
# What happesn when we run:
trip = RoadTrip()
print(trip.predict_the_future())

'''
A:
We have another class RoadTrip defined on line 20 that inherits from Oracle.
This class overwrites our choices function with a new list of strings.
line 32 will print: either of the roadtrip choices phrases.
This is because we overwrite the choices method in RoadTrip. The predict the 
future method can still be called on our RoachTrip object since it inherits from
Oracle but Python will search the RoadTrip class for the choices method first 
before falling back on the choices method in Oracle.
'''