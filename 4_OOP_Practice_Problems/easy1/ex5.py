'''
Which of the following classes would create objects that have an instance
variable. How do you know?
'''
class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

'''
A:
Only Pizza would create objects that have instance variables. We know because
it assigns a value to self.my_name where self refers to the object that is calling
the init method, ie the object that is being instantiated.
'''

# Can use vars() to see what instance variables exist in our objects:
print(vars(Fruit('orange')))     # {}
print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}
