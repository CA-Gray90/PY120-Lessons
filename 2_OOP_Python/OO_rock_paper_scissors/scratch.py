class DisplayMixin:
    def display(self):
        print('*' * 10)
        print(f'I am {self.name}, and I am a {self.__class__.__name__}.')
        print(f'I am {self.age} years old.')
        print('*' * 10)

class Animal(DisplayMixin):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

dog = Dog('Teddy', 3)
cat = Cat('Fluffy', 5)
bird = Bird('Squawky', 20)

dog.display()
dog.age = 10
dog.display()

cat.display()
bird.display()
bird.age = 40
bird.display()