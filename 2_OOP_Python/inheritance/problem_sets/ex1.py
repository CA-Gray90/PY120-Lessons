# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"
class Pet:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'
    
    def fetch(self):
        return 'fetching!'

class Cat(Pet):
    def speak(self):
        return 'meow!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

# teddy = Dog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!
# frenchie = Bulldog()
# print(frenchie.speak())
# print(frenchie.sleep())

# pet = Pet()
# dave = Dog()
# bud = Bulldog()
# kitty = Cat()

# print(pet.run())              # running!
# print(kitty.run())            # running!
# print(kitty.speak())          # meow!
# try:
#     kitty.fetch()
# except Exception as exception:
#     print(exception.__class__.__name__,':', exception, "\n")
#     # AttributeError 'Cat' object has no attribute 'fetch'

# print(dave.speak())           # bark!

# print(bud.run())              # running!
# print(bud.sleep())             # "snoring!"

# Class heirachy:
'''
                 Pet
                 - speak
                 - sleep
                 - run
                 - jump
             /        \
        Cat              Dog
        - speak          - speak
                         - fetch
                            \
                             Bulldog
'''

# MRO - Method Resolution Order is the order that Python will search through
# the class and superclasses of a class (traverse the class heirachy) for a
# method definition. If it doesnt find a method, it will return an AttributeError.

Bulldog.mro() # -> [Bulldog, Dog, Pet, object]
Cat.mro() # -> [Cat, Pet, Object]