# File name: personClass.py
# Author: (use your name, of course)
# Description: Defines the attributes of a  Person.


class University:
    def __init__(self, name):
        self.set_name(name)
        self.students = []
        self.teachers = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_teachers(self):
        return self.teachers
