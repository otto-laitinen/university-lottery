# File name: studentClass.py
# Author:  Salli Saarinen
# Description: Inherits from personClass,
# defines attributes of students

import personClass
# import universityClass


class Student(personClass.Person):

    # initializes the different methods + inherited ones from personClass
    def __init__(self, first_name, last_name, age, tickets, institute, credits):
        personClass.Person.__init__(self, first_name, last_name, age, tickets)
        self.__institute = institute
        self.__credits = credits
        # Adds this instance of Student to University's (institute's) list of students
        institute.add_student(self)

    def set_institute(self, institute):
        self.__institute = institute

    def set_credits(self, credits):
        self.__credits = credits

    def get_institute(self):
        return self.__institute

    def get_credits(self):
        return self.__credits
