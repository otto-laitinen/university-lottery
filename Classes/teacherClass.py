# File name: teacherClass.py
# Author: Salli Saarinen, Otto Laitinen, Thomás Rizzi Omura
# Description: Inherits from personClass,
# defines the attributes of a teacher.

import personClass


class Teacher(personClass.Person):

    # initializes the different methods + inherited ones from personClass
    def __init__(
        self, 
        first_name, 
        last_name, 
        age, 
        tickets, 
        institute, 
        days_off):
        personClass.Person.__init__(self, first_name, last_name, age, tickets)
        self.__institute = institute
        self.__days_off = days_off
        # Adds this instance of Teacher to University's (institute's) list of teachers
        institute.add_teacher(self)

    #set and get for institute is there, so the students 
    # and teachers are differentiate from 'normal' people
    def set_institute(self, institute):
        self.__institute = institute
    #the set and get from days_off are used for the lottery winners prize
    def set_days_off(self, days_off):
        self.__days_off = days_off

    def get_institute(self):
        return self.__institute

    def get_days_off(self):
        return self.__days_off