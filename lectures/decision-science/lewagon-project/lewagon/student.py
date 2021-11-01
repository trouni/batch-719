from datetime import date


class Student:
    school = "Le Wagon"  # class attribute

    def __init__(self, name, age):
        # instance variables / attributes
        self.name = name.capitalize()
        self.age = age

    # instance method
    def says(self, thing):
        print(f"{self.name} says {thing}")

    # Student.says(kyle, 'hi!!!!') is equivalent to kyle.says('hi!!!!')
    # Class.method(instance, other_args) <=> instance.method(other_args)

    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)
