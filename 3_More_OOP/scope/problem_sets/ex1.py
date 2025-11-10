class Dog:
    def __init__(self, breed):
        self._breed = breed
    
    def get_breed(self):
        return self._breed

retriever = Dog('Golden Retriever')
poodle = Dog('Poodle')

print(retriever.get_breed())
print(poodle.get_breed())

bulldog = Dog(None)
bulldog._breed = 'Bulldog'
print(bulldog.get_breed())