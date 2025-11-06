class Cat:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.lower() == other.name.lower()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.lower() != other.name.lower()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() <= other.name.casefold()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() > other.name.casefold()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() >= other.name.casefold()

cat1 = Cat('fluffy')
cat2 = Cat('FluFFy')
cat3 = Cat('Bobby')
cat4 = Cat('Bobby Junior')

print((cat1 > cat2) == False)
print((cat1 >= cat2) == True)
print((cat3 > cat1) == False)
print((cat1 < cat2) == False)
print((cat3 <= cat1) == True)
print((cat4 > cat3) == True)