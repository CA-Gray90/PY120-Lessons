class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    # @classmethod
    # def hi(cls):
    #     super().greet(cls, "Hi")

    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Test 1:
hello = Hello() # Assign hello to instance of Hello
hello.hi()      # prints 'Hello'

# # Test 2:
# hello = Hello()
# hello.bye()     # AttributeError: hello object has no attribute 'bye'

# # Hello doesn't define a bye() method and Greeting, the class it inherits from
# # also doesn't define one.

# # Test 3:
# hello = Hello()
# hello.greet()   # TypeError: expecting 2 arguments but only recieved one (self, no message argument given)

# # Test 4:
# hello = Hello()
# hello.greet('Goodbye')  # prints 'Goodbye'

# Test 5:
Hello.hi() # TypeError: Expecting 1 argument but none given, needs an object instance to be passed to it as 'self'
