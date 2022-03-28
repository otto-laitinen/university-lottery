# File name: studentClass.py
# Author:  Salli Saarinen
# Description: Inherits from personClass, 
# defines attributes of students

import personClass

class Student(personClass.Person):
    
    #initializes the different methods + inherited ones from personClass
    def __init__(self,first_name,last_name,age,institute,role):
        personClass.Person.__init__(first_name,last_name,age)
        self.__institute = institute
        self.__role = role
    
    #sets institute and role
    def set_institute(self,institute):
        self.__institute = institute
    def set_role(self,role):
        self.__role = role
    
    #gets institute and role
    def get_institute(self):
        return self.__institute
    def get_role(self):
        return self.__role
