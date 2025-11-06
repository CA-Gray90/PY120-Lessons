class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector((self.x + other.x), (self.y + other.y))
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector((self.x - other.x), (self.y - other.y))
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector((self.x * other), (self.y * other))
    
    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector((self.x * other), (self.y * other))
    
    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.x *= other
        self.y *= other
        return self

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'