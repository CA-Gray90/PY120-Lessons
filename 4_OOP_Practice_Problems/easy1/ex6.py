'''
Without running the following code, can you determine what the following code
will do? Explain why you will get those results.
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

oracle = Oracle()
print(oracle.predict_the_future())

'''
A:
line 21 will print: either of the phrases in choices. 
We can call an instance method from within another instance method by appending
the method name with self. Therefore line 10 refers to the choices method defined
on line 12 by calling self.choices.
'''