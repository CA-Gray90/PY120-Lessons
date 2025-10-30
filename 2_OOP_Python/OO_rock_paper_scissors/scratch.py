class Move:
    def __init__(self):
        self._beats = None
    
    def __str__(self):
        return NotImplemented
    
    # Each Move subclass knows who it can beat (using comparison operators)
    def __gt__(self, other):
        if isinstance(other, Move):
            return str(other) in self._beats
        else:
            return NotImplemented

class Rock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('scissors', 'lizard')

    def __str__(self):
        return 'rock'

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'spock')

    def __str__(self):
        return 'paper'

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('lizard', 'paper')

    def __str__(self):
        return 'scissors'

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('paper', 'spock')

    def __str__(self):
        return 'lizard'

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'scissors')

    def __str__(self):
        return 'spock'

rock = Rock()
paper = Paper()
scissors = Scissors()
lizard = Lizard()
spock = Spock()

print((rock > scissors) == True)
print((spock > scissors) == True)
print((paper > spock) == True)
print((lizard > spock) == True)
print((lizard > paper) == True)
print((scissors > paper) == True)
print((rock > lizard) == True)
print((scissors > lizard) == True)
print((spock > rock) == True)
print((paper > rock) == True)
print((rock < scissors) == False)
print((spock < scissors) == False)
print((paper < spock) == False)
print((lizard < spock) == False)
print((lizard < paper) == False)
print((scissors < paper) == False)
print((rock < lizard) == False)
print((scissors < lizard) == False)
print((spock < rock) == False)
print((paper < rock) == False)