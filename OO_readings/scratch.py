class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name
    
fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')
misty = Cat('Misty')

print(fluffy != misty)          # true
print(fluffy == fluffy2)       # true
print(fluffy.__eq__(fluffy2)) # true