# File name: studentClass.py
# Author:  Salli Saarinen, Otto Laitinen, Thomás Rizzi Omura
# Description: Inherits from personClass,
# defines attributes of students

import personClass

class Student(personClass.Person):

    # initializes the different methods + inherited ones from personClass
    def __init__(
        self, 
        first_name, 
        last_name, 
        age, 
        tickets, 
        institute, 
        credits):
        personClass.Person.__init__(self, first_name, last_name, age, tickets)
        self.__institute = institute
        self.__credits = credits
        # Adds this instance of Student to University's 
        # (institute's) list of students
        institute.add_student(self)

    #set and get for institute is there, so the students 
    # and teachers are differentiate from 'normal' people
    def set_institute(self, institute):
        self.__institute = institute
    #the set and get fro credits are used for the lottery winners prize
    def set_credits(self, credits):
        self.__credits = credits

    def get_institute(self):
        return self.__institute

    def get_credits(self):
        return self.__credits
