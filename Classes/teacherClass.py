# File name: teacherClass.py
# Author: (use your name, of course)
# Description: Inherits from personClass,
# defines the attributes of a teacher.

import personClass


class Teacher(personClass.Person):

    # initializes the different methods + inherited ones from personClass
    def __init__(self, first_name, last_name, age, tickets, institute, days_off):
        personClass.Person.__init__(self, first_name, last_name, age, tickets)
        self.__institute = institute
        self.__days_off = days_off
        # Adds this instance of Teacher to University's (institute's) list of teachers
        institute.add_teacher(self)

    def set_institute(self, institute):
        self.__institute = institute

    def set_days_off(self, days_off):
        self.__days_off = days_off

    def get_institute(self):
        return self.__institute

    def get_days_off(self):
        return self.__days_off