'''
Create a class called Animal with a single instance method called speak that
takes a string argument and prints that argument to the terminal.

Now create two other classes that inherit from Animal, one called Cat and one
called Dog. The Cat class should have a meow instance method that takes no
arguments and prints Meow!. The Dog class should have a bark instance method
that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal
class's speak method when implementing the Cat and Dog classes. Don't invoke the
print function in either of the subclasses.
'''

class Animal:
    def speak(self, sentence):
        print(sentence)
    
class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

cat1 = Cat()
dog1 = Dog()

cat1.meow()
dog1.bark()
'''
speak method is inherited by both Cat and Dog. No need to call super().speak()
'''