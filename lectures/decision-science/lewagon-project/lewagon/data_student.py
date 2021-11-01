from lewagon.student import Student


class DataStudent(Student):
    course = "data"

    def __init__(self, name, age, nerd):
        super().__init__(name, age)
        self.nerd = nerd
