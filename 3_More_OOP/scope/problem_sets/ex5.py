'''
Define a Student class that has a class variable named school_name. You should
initialize the school name to 'Oxford'. After defining the class, instantiate
an instance of the Student class and print the school name using that instance.
'''

class Student:
    school_name = 'Oxford'
    
    @classmethod
    def school(cls):
        return cls.school_name

    def __init__(self, name):
        self.name = name

print(Student.school_name)
print(Student.school())

# gary = Student('Gary')
# henry = Student('Henry')

# print(gary.name, gary.__class__.school_name)
# print(henry.name, henry.__class__.school_name)