# File name: personClass.py
# Author: (use your name, of course)
# Description: Defines the attributes of a  Person.


class University:
    def __init__(self, name):
        self.set_name(name)
        self.students = []  # list of Student objects
        self.teachers = []  # list of Teacher objects

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_student(self, students):
        pass

    def delete_students(self, teachers):
        pass

    def add_teacher(self, teachers):
        # add a teacher object to teachers list
        # also add this instance of this class as an "institute" for the teacher
        pass

    def delete_teachers(self):
        # delete a teacher object from the teachers list, also set institute of
        # the teacher to None (or possibly just delete the whole object)
        pass
